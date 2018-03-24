mapping = {'2': 1, '0': 3, '3': 2, '1': 0}

def getBlocks(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]

def decrypt_letter2(ciphertext):
    ciphertext = getBlocks(ciphertext,4)
    quart = []
    plaintext = []
    for i in range(len(ciphertext)+1):
        for j in range(4):
            try:
                quart.insert(mapping[str(j%4)],ciphertext[i][j])
            except:
                break
        plaintext += quart
        quart = []
    return reduce(lambda x,y:x+y, plaintext)

if __name__ == '__main__':
    ciphertext = open("mtc3-esslinger-16-cipher-en.txt", "r").read().replace(" ","")
    print(decrypt_letter2(ciphertext))
    
