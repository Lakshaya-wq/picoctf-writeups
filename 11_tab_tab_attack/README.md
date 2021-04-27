# Tab, Tab, Attack

> Solution: Unzip the given zip file, cd in the first dir and keep pressing tabs until the directories end ;). You will find an executable in the last directory, run it and get your flag. I decide to do it programtically. Here's my script:

```python
#!/usr/bin/env python3

import subprocess

bin_path = subprocess.check_output(["find | grep fang-of-haynekhtnamet"], shell=True).decode('latin-1').strip()
flag = subprocess.check_output([f"{bin_path} | grep pico"], shell=True).decode('latin-1').replace("*ZAP!*", "").replace(" ", "")
print(flag) # picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
```