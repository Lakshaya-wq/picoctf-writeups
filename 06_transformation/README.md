# Transformation

> Solution: Decode the encoded string by reversing the given python code. I was stuck at this so I had a look at [this](https://vishnuram1999.github.io/transformation_pico_ctf_2021.html) writeup, and came up with this solution:
```python
#!/usr/bin/env python3
encoded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"

flag = []

for i in range(len(encoded)):
	flag.append(chr(ord(encoded[i])>>8))
	flag.append(chr((ord(encoded[i]))-((ord(encoded[i])>>8)<<8)))

print(''.join(flag))
```