from challenge_9 import PKCS_7

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

def isValidPKCS_7(paddedtext):
    block_size = 16
    ctext = []
    for pt in range(len(paddedtext)):
        ctext.append(paddedtext[pt])
    chunk = ctext[-1]
    ctext.remove(ctext[-1])
    if chunk == 0 or int(toHex(chunk)) != len(paddedtext) % block_size:
        raise ValueError('Padding is wrong')
    part = []
    part.append(chunk)
    while ctext[-1] == chunk:
        part.append(ctext[-1])
        ctext.remove(ctext[-1])
    if len(part) != len(paddedtext) % block_size:
        raise ValueError('Padding is wrong')
    else:
        print("Padding is correct")
        return ctext


if __name__ == '__main__':
    text = "YELLOW SUBMARINE"
    paddedtext = PKCS_7(text,20) 
    unpadded = isValidPKCS_7(paddedtext) #or "ICE ICE BABY\x05\x05\x05\x05" or "ICE ICE BABY\x01\x02\x03\x04".
                                         #they are not correct
    print(unpadded)
