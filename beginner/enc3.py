import base64

x = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'



y = bytes.fromhex(x)

print(y)

z = base64.b64encode(y)

print(z)