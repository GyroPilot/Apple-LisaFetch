LisaFetch 0.1, update 1 (3 November 2026, release build REV C)      tool 419325
Same LisaFetch 0.1 program with these changes, tested on a Lisa 2/10 through an ESProFile running ESPFuji on 3
November 2026; the floppy LISAFETCH_0_1.dc42 replaces the earlier one of the same name:
- A failed connection through an ESProFile now shows the ESProFile's own reason ("the drive said: ...")
  instead of only "status 207".

--------------------------------------------------------------------------------------------------------------

LisaFetch 0.1 (2 November 2026)      tool 419325      Tim O'Connor (bmwcyclist)

Fetches a plain text file from the web and saves it on your Lisa as a Workshop .TEXT file, ready for the
Editor and the Pascal compiler.  Asked for by Chris Rupnik, who wanted a way to get source text files onto
a Lisa.

  1. Copy LisaFetch from LISAFETCH_0_1.dc42 to your ProFile (or run it from the floppy).
  2. Open it, press G, type the address of a plain text file, e.g. a raw GitHub file:
       https://raw.githubusercontent.com/GyroPilot/Apple-LisaFuji/main/sources/LFJ-COMP.TEXT
     and press RETURN.
  3. Type a name for it on the Lisa (".TEXT" is added if you leave it off) and press RETURN.
     A name alone goes beside the tool; -#12-SRC/MAIN.TEXT style paths are used as typed.
  4. It asks before replacing a file (Lisa names ignore case: COMP.TEXT and Comp.Text are the same file).
     The new file replaces the old one only when it has arrived whole.
  R fetches the same address again; ? is help.

The network: an ESPFuji ESProFile (put the tool on the drive's volume; run the ESPFuji test tool there once),
an RS-232 FujiNet on Serial B (or A), or a LisaNet.  The top line says which one it found.  Up to 32 KB per
file through an ESPFuji drive; no fixed limit through a serial FujiNet.  Plain text only; tabs become spaces;
characters outside plain ASCII become '?'.  The Workshop sees the file at once; the Office System desktop does
not show plain files as icons.

Tested: on a Lisa 2/10 through an ESProFile running ESPFuji 1.1 beta, 2 November 2026: a 42-line exec file
from GitHub saved as a Workshop text file, and the "Replace it?" question when fetching to the same name
again.  Also built with the Workshop 3.0 and run in LisaEm through a serial FujiNet stand-in, where the saved
file matched GitHub's line for line.

New since the 30 October test build: the ESPFuji mailbox is looked for as "ESPFuji Mailbox" first, then
MAILBOX.DATA, so existing setups keep working; the floppy's tool name no longer has trailing spaces.

Source, licence (MIT) and the build recipe: https://github.com/GyroPilot/Apple-LisaFetch
