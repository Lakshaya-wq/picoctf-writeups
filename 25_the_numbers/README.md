# The Numbers

> Solution: Convert the given alphabet's *index* into its respective alphabet. Note down the index values from the picture given. Then we check whether the given character is a string or number. If its a number then we get the alphabet from the value after subtracting 1 from it **(List index starts from 0)**. If its a letter then we append it as it is. Becuase the flag format is in capital we have to submit the flag in capital.


```python
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
```