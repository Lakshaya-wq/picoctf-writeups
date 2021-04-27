#!/usr/bin/env python3
encoded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"

flag = []

for i in range(len(encoded)):
	flag.append(chr(ord(encoded[i])>>8))
	flag.append(chr((ord(encoded[i]))-((ord(encoded[i])>>8)<<8)))

print(''.join(flag))