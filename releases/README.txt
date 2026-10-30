LisaFetch 0.1 (test build, 30 October 2026)      tool 419325      Tim O'Connor (bmwcyclist)

Fetches a plain text file from the web and saves it on your Lisa as a Workshop .TEXT file, ready for the
Editor and the Pascal compiler.

  1. Copy LisaFetch from LISAFETCH_0_1.dc42 to your ProFile (or run it from the floppy).
  2. Open it, press G, type the address of a plain text file, e.g. a raw GitHub file:
       https://raw.githubusercontent.com/GyroPilot/Apple-LisaFuji/main/sources/LFJ-COMP.TEXT
     and press RETURN.
  3. Type a name for it on the Lisa (".TEXT" is added if you leave it off) and press RETURN.
     A name alone goes beside the tool; -#12-SRC/MAIN.TEXT style paths are used as typed.
  4. It asks before replacing a file (Lisa names ignore case: COMP.TEXT and Comp.Text are the same file).
     The new file replaces the old one only when it has arrived whole.

The network: an ESPFuji ESProFile (put the tool on the drive's volume; run the ESPFuji test tool there once),
an RS-232 FujiNet on Serial B (or A), or a LisaNet.  Up to 32 KB per file through an ESPFuji drive; no fixed
limit through a serial FujiNet.  Plain text only; tabs become spaces; characters outside plain ASCII become '?'.
The Workshop sees the file at once; the Office System desktop does not show plain files as icons.

Tested so far: built with the Workshop 3.0 and run on the Lisa Office System in LisaEm, fetching a GitHub file
through a serial FujiNet stand-in; the saved file matched GitHub's line for line.  NOT yet run on a real Lisa:
please say what happens, good or bad.
