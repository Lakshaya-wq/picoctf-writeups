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
print(flag_start + key + closing_brace)