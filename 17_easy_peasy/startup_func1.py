import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)
	print(key_location)
	print(stop)

	key = kf[start:stop]
	print(key)
	key_location = stop
	print(key_location)

	# result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	result = "".join(list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key)))
	print(result)
	# print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

if __name__ == '__main__':
	print(startup(0))