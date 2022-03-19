import math

#c1
#su dung thu vien
#print(math.gcd(66528, 52920))

def gcd(a, b):
	if b == 0:
		return a 
	else:
		return gcd(b, a%b)

print(gcd(66528, 52920))