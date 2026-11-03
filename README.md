# LisaFetch

Fetches a text file from the web and saves it on the Apple Lisa as a Workshop **.TEXT** file, ready for the Editor
and the Pascal compiler. Press G, type the address of a plain text file (a raw GitHub file, a file on your own
server), then a name for it on the Lisa. Asked for by Chris Rupnik: "Please tell me that this can be used to
transfer source text files onto a Lisa somehow."

Tool number **419325** in the GyroPilot series. Lisa Pascal, Workshop 3.0, Lisa Office System 3.1.

## How it reaches the network

The same FnBus unit as LisaFuji 1.2: through an **ESPFuji ESProFile** (found by itself when the tool is on the
drive's volume; run the ESPFuji test tool there once), an **RS-232 FujiNet** on Serial B or A, or a **LisaNet**.
Through an ESPFuji drive a file can be up to 32 KB; through a serial FujiNet there is no fixed limit.

## What it writes

A Workshop text file: a 1024-byte header page of nulls, then 1024-byte pages of whole lines, each line ended by a CR,
each page filled with nulls. LF, CR LF and CR all end a line; a tab becomes spaces to the next column of 8; a line
longer than 1000 characters is cut in two; bytes outside 32..126 become '?' (other controls are dropped). The file
is written to LISAFETCH.TEMP and renamed only when the fetch is complete, so a failed fetch never harms a file that
was there. A name alone goes beside the tool; a name starting with - (e.g. -#12-SRC/MAIN.TEXT) is used as a path;
.TEXT is added to a name without a dot. Lisa file names ignore case: it asks before replacing a file.

The Workshop sees the file at once (Filemgr, the Editor, Pascal). The Office System desktop does not show plain files
as icons.

## Status

**0.1, 2 November 2026 (release build REV B).** Tested on a Lisa 2/10 through an ESProFile running ESPFuji 1.1 beta:
a 42-line exec file from GitHub saved as a Workshop text file, and the "Replace it?" question when fetching to the
same name again. Also compiled and installed with the Workshop 3.0 in LisaEm; run there through PCFuji, the saved file
matched GitHub's line for line, and its output is byte-identical to the Workshop text that TorZidan's
LisaFileSystemTool writes for the same file.

New since the 30 October test build: the ESPFuji mailbox is looked for as "ESPFuji Mailbox" first, then MAILBOX.DATA;
the release floppy's tool name no longer has trailing spaces.

## Building

Copy `sources/LFT-*.TEXT` to the Lisa as LFT/GLOBALS.TEXT, LFT/FNBUS.TEXT, LFT/MAIN.TEXT, LFT/ALERTS.TEXT,
LFT/COMP.TEXT, LFT/LINK.TEXT, LFT/MAKE.TEXT, LFT/INSTALL.TEXT and `icon/LFTICONA.BIN` as LFT/ICON.BIN, then
`R <LFT/MAKE` and `R <LFT/INSTALL`.

`tools/serve_file.py` is a tiny FujiNet over TCP that serves one file, for testing with the PC harness or PCFuji.

MIT licence. Tim O'Connor (bmwcyclist / GyroPilot), 2026.
