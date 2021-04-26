#!/usr/bin/env python3
from pwn import *

host, port = "mercury.picoctf.net", 22342
context.log_level = 'critical'

s = remote(host, port)

ascii_values = str(s.recv().decode('latin-1')).replace(' ', '').split('\n')
flag = []

for char in ascii_values:
	try:
		flag.append(str(chr(int(char))))

	except ValueError:
		break

print(''.join(flag))

s.close()