#Vì đề bài cho hint là xor với 1 single byte, chắc là nó sẽ nằm trong khoảng từ 1 -> 256 ý nên ta làm thôi^^

key1 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

#decode hex
s = [o for o in bytes.fromhex(key1)]
print(s)

#lặp tới 256
for order in range(256):
	possible_flag_ord = [order ^ o for o in s]
	fake_flag = "".join(chr(o) for o in possible_flag_ord)

	if(fake_flag.startswith("crypto")):
		real_flag = fake_flag
		break

print(real_flag)