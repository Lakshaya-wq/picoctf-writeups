# crackme-py

> Solution: rot47 decode the given `bezos_cc_secret`.

```python
#!/usr/bin/env python3

rot47_flag = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN"

alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_rot47(string):

    rotate_const = 47

    decoded = ""

    # decode loop
    for c in string:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    return decoded

if __name__ == '__main__':
	print(decode_rot47(rot47_flag)) # picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}
```