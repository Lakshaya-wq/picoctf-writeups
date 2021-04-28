import os

for item in os.listdir():
	if os.path.isdir(item):
		try:
			print(f"[{item}](./{item}/)")
		except IndexError:
			pass
