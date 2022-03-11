string = "label"
integer = 13

#bien doi ve ki tu char -> decimal l = 108....
unicode_repr = [ord(c) for c in string]
print(unicode_repr)

#xor ^ tung ki tu voi 13
xor_unicode = [13 ^ i for i in unicode_repr]
print(xor_unicode)

# decimal -> char chr()
xor_string = "".join(chr(o) for o in xor_unicode)

flag = "crypto{" + xor_string + "}"

print(flag)