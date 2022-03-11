key = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

key = bytes.fromhex(key)

print(key)

flag_format = b"crypto{"
key1 = [o1 ^ o2 for(o1, o2) in zip(key, flag_format)] + [ord("y")]

#print(ord("y"))


flag = []
key_len = len(key1)
for i in range(len(key)):
	flag.append(key[i] ^ key1[i % key_len])

flag = "".join(chr(o) for o in flag)

print(flag)

