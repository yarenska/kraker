
def XOR(a,b):
    XORed = []
    for i in range(max(len(a), len(b))):
        XORed_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        XORed.append(hex(XORed_value)[2:])
    return ''.join(XORed)


text = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"
mapping = {0: 'I', 1: 'C', 2: 'E'}

for i in range(0,len(text)-3):
    key += mapping[i%3]
    
print(XOR(text,key))
