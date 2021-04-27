# GET aHEAD

> Solution: Make a `HEAD` request to the url. 

When looking at the [webpage](http://mercury.picoctf.net:15931/), it turns out to be pretty simple. Making a `POST` request to it changes the color to blue, while a `GET` request changes it to red. I spent a while figuring it out, but before giving up I read the name of the challenge again. The answer is in the title itself ***GET*** a***HEAD***. Both of these turn out to be HTTP request methods. So, you can
```bash
curl "http://mercury.picoctf.net:15931/" --head
```
It returns the flag: *picoCTF{r3j3ct_th3_du4l1ty_82880908}*

So I created a [python script](./solution.py).
Very simple.

```python
#!/usr/bin/env python3

import requests

response = requests.head("http://mercury.picoctf.net:15931")

print(response.headers['flag']) # picoCTF{r3j3ct_th3_du4l1ty_82880908}
```