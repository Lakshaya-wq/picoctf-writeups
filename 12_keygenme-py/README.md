# keygenme-py

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True

```
> Solution: In the source code, it is clear that it has a static `key_part_static1_trial`, dynamic `key_part_dynamic1_trial`, and a static `key_part_static2_trial`. The key is the flag itself. The dynamic part however, is just some certain indexes of the sha256 hash of the username `FREEMAN`. Pretty simple to solve:

```python
#!/usr/bin/env python3

import hashlib


flag_start = "picoCTF{1n_7h3_|<3y_of_"
magic_key = "xxxxxxxx"
closing_brace = "}"

key = ""

trial_username = b"FREEMAN"

positions = [4, 5, 3, 6, 2, 7, 1, 8]

for i in positions:
	key += hashlib.sha256(trial_username).hexdigest()[i]

final_key = flag_start + key + closing_brace
print(flag_start + key + closing_brace) # picoCTF{1n_7h3_|<3y_of_0d208392}
```