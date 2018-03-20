
def fixedXOR(a,b):
    XORed = []
    for i in range(max(len(a), len(b))):
        XORed_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        XORed.append(hex(XORed_value)[2:])
        print(hex(XORed_value)[2:])
    return ''.join(XORed)


if __name__ == "__main__":
    text1 = "1c0111001f010100061a024b53535009181c"
    text2 = "686974207468652062756c6c277320657965"
    result = fixedXOR(text1.decode("hex"),text2.decode("hex"))
    print(result)
    
