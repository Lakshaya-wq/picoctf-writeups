# Matryoshka Doll

> Solution: Keep extracting the files from the original image file until you find the flag.txt. Here is my little script :D.

```bash
#!/usr/bin/env bash
# sudo apt install binwalk
export oldwd=`pwd`
binwalk --dd='.*' -e dolls.jpg >/dev/null
cd _dolls.jpg.extracted/
cd base_images/
binwalk --dd='.*' -e 2_c.jpg >/dev/null
cd _2_c.jpg.extracted/
cd base_images/
binwalk --dd='.*' -e 3_c.jpg >/dev/null
cd _3_c.jpg.extracted/
cd base_images/
binwalk --dd='.*' -e 4_c.jpg >/dev/null
cd _4_c.jpg.extracted/
printf "\n" >> flag.txt
cat flag.txt # picoCTF{96fac089316e094d41ea046900197662}
cd $oldwd
```