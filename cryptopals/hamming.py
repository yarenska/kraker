
def xor (a,b):
    XORed = []
    for i in range(max(len(a), len(b))):
        print(ord(a[i%len(a)]), ord(b[i%len(b)]))
        XORed_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        XORed.append(hex(XORed_value)[2:])
    return ''.join(XORed)

def hamming(text1,text2):
    count = 0
    my_hexdata = xor(text1, text2)
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
   
    for bit in bin(int(my_hexdata, scale))[2:].zfill(num_of_bits):
        if bit == '1':
            count = count+1
    return count
        
if __name__ == '__main__':
    text1 = "this is a test"
    text2 = "wokka wokka!!!"
    print(text1,text2)
    count = hamming(text1,text2)
    print(count)

