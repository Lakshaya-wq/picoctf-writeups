# Static ain't always noise

> Solution: Run the given [bash script](./ltdis.sh) with the filename of the binary as the argument. Then in the [static.ltdis.strings.txt](./static.ltdis.strings.txt) file, line 15 you can find your flag in plain text.

```bash
./ltdis.sh static 
# Attempting disassembly of static ...
# Disassembly successful! Available at: static.ltdis.x86_64.txt
# Ripping strings from binary with file offsets...
# Any strings found in static have been written to static.ltdis.strings.txt with file offset

cat static.ltdis.strings.txt | grep picoCTF
#    1020 picoCTF{d15a5m_t34s3r_98d35619}
```