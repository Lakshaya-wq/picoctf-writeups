#!/usr/bin/env python3

import requests

response = requests.head("http://mercury.picoctf.net:15931")

print(response.headers['flag']) # picoCTF{r3j3ct_th3_du4l1ty_82880908}