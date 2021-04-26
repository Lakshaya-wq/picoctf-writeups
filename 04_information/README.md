# Information

> Solution: Use exiftool to extract the metadata. The license looks something like base64 encoded. So,
```bash
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
# picoCTF{the_m3tadata_1s_modified}
```