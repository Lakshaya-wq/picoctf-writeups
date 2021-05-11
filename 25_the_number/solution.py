#!/usr/bin/env python3

import string

ascii_flag = [16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]
alphabets = string.ascii_uppercase
flag = []

for char in ascii_flag:
	if type(char).__name__ == "int":
		flag.append(alphabets[(char - 1)])
	else:
		flag.append(char)
print(''.join(flag)) # PICOCTF{THENUMBERSMASON}