# Nice Netcat

> Solution: The characters being received from the host are ascii representations of their characters. So knowing this we can decode the value in each line to its ascii char to form a flag.

```python
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

print(''.join(flag)) # picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}

s.close()
```