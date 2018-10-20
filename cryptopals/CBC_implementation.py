from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import base64
import StringIO

def padding(text,block):
    if(len(text) < block):
        pad_time = block - len(text)
    else:
        pad_time =  block % len(text)
    output = StringIO.StringIO()
    for i in range(0,pad_time):
        output.write(chr(int(pad_time)))
    
    return text+output.getvalue()

def closest_dividend(n):
    i = 0
    while(i < n):
        i = i+16
    return i

def getBlocks(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]

def CBC_decrypt(ciphertext,key,IV):
    ECB_cipher = AES.new(key, AES.MODE_ECB) 
    blocksize = 16
    ciphertext = getBlocks(ciphertext, blocksize)
    plainXOR = IV
    plaintext = []

    for i in range(len(ciphertext)):
        cipherBlock = ciphertext[i]
        plainBlock = strxor(ECB_cipher.decrypt(cipherBlock),plainXOR) 
        plaintext += plainBlock
        plainXOR = cipherBlock
    return reduce(lambda x,y:x+y, plaintext)


def CBC_encrypt(plaintext,key,IV):
    ECB_cipher = AES.new(key, AES.MODE_ECB) 
    blocksize = 16
    plaintext = getBlocks(plaintext, blocksize)
    cipherXOR = IV
    ciphertext = []

    for i in range(len(plaintext)):
        plainBlock = plaintext[i]
        cipherBlock = ECB_cipher.encrypt(strxor(cipherXOR,plainBlock)) 
        ciphertext += cipherBlock
        cipherXOR = cipherBlock
    return reduce(lambda x,y:x+y, ciphertext)

if __name__ == '__main__':
    plaintext = "**Vanilla ice ice baby**" #i made that up to see whether my algorithm works or not
    if(len(plaintext) % 16 != 0):
        n = closest_dividend(len(plaintext))
        plaintext = padding(plaintext,n)
    ciphertext = CBC_encrypt(plaintext,"YELLOW SUBMARINE",("0" * 16)) #you can encrypt with iv = "fake 0th ciphertext block" contains all 0's
    back_plaintext = CBC_decrypt(ciphertext,"YELLOW SUBMARINE",("0" * 16)) #you can decrypt back
    if back_plaintext != plaintext:
        raise Exception("Couldn't convert to plaintext back.")
    else:
        print("Plaintext: " + plaintext)
        print("Encrypted: " + ciphertext)
        print("Decrypted: " + back_plaintext)
