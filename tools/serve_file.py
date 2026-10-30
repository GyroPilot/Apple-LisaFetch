#!/usr/bin/env python3
"""serve_file.py PORT FILE [CHUNK]  -- a tiny FujiNet for the LisaFetch PC test (30-Oct-2026).
Answers FujiBus frames on a TCP port like an RS-232 FujiNet would for one N1: fetch:
  70 xx (FujiNet control)  -> ACK (adapter config 0xE8 gets 140 bytes, WiFi 0xFA gets 3 = connected)
  71 'O' OPEN              -> ACK, and FILE is the body from now on (the URL is printed)
  71 'S' STATUS            -> ACK [waiting lo, hi, connected, status]: status 1 while bytes are left, 136 at the end
  71 'R' READ n            -> ACK and the next n bytes (at most CHUNK are reported waiting at once, default 300)
  71 'C' CLOSE             -> ACK
Every request is printed.  One connection at a time; it keeps serving until killed."""
import socket, sys
from fujibus import encode, decode, END

PORT = int(sys.argv[1]); BODY = open(sys.argv[2], "rb").read()
CHUNK = int(sys.argv[3]) if len(sys.argv) > 3 else 300
STOPAT = int(sys.argv[4]) if len(sys.argv) > 4 else 0   # go silent once this many bytes are sent (0 = never)
ACK = 0x06


def frames(conn):
    buf = bytearray()
    while True:
        b = conn.recv(4096)
        if not b:
            return
        buf += b
        while True:
            try:
                s = buf.index(END)
            except ValueError:
                buf.clear(); break
            try:
                e = buf.index(END, s + 1)
            except ValueError:
                del buf[:s]; break
            fr = bytes(buf[s:e + 1]); del buf[:e]
            if len(fr) > 2:
                yield fr


def main():
    srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", PORT)); srv.listen(1)
    print("serving %d bytes on %d" % (len(BODY), PORT), flush=True)
    while True:
        conn, _ = srv.accept(); pos = len(BODY); opened = False
        print("-- connection", flush=True)
        for fr in frames(conn):
            try:
                dev, cmd, params, payload = decode(fr)
            except Exception as ex:
                print("bad frame", fr.hex(), ex, flush=True); continue
            if STOPAT and opened and pos >= STOPAT:
                print('(silent now, at %d)' % pos, flush=True); continue
            if dev == 0x70:
                pl = b""
                if cmd == 0xE8:
                    pl = bytearray(140); pl[0:5] = b"MyNet"; pl[125:130] = b"1.6.0"; pl = bytes(pl)
                elif cmd == 0xFA:
                    pl = b"\x03"
                print("70 %02X -> ACK" % cmd, flush=True)
                conn.sendall(encode(0x70, ACK, payload=pl))
            elif dev == 0x71 and cmd == 0x4F:
                print("OPEN", payload.rstrip(b"\0").decode("latin-1"), params, flush=True)
                pos = 0; opened = True
                conn.sendall(encode(0x71, ACK))
            elif dev == 0x71 and cmd == 0x53:
                left = len(BODY) - pos if opened else 0
                w = min(left, CHUNK)
                st = bytes([w & 0xFF, w >> 8, 1 if left else 0, 1 if left else 136])
                print("STATUS -> waiting %d, status %d" % (w, st[3]), flush=True)
                conn.sendall(encode(0x71, ACK, payload=st))
            elif dev == 0x71 and cmd == 0x52:
                n = params[0] if params else 0
                chunk = BODY[pos:pos + n]; pos += len(chunk)
                print("READ %d -> %d bytes (at %d of %d)" % (n, len(chunk), pos, len(BODY)), flush=True)
                conn.sendall(encode(0x71, ACK, payload=chunk))
            elif dev == 0x71 and cmd == 0x43:
                print("CLOSE", flush=True); opened = False
                conn.sendall(encode(0x71, ACK))
            else:
                print("other %02X %02X %s -> ACK" % (dev, cmd, params), flush=True)
                conn.sendall(encode(dev, ACK))
        conn.close()


main()
