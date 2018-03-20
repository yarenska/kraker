from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import base64

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
    '''
    plaintext = "I like chocolate and ice cream.." #i made that up to see whether my algorithm works or not
    ciphertext = CBC_encrypt(plaintext,"YELLOW SUBMARINE",("0" * 16)) #you can encrypt
    back_plaintext = CBC_decrypt(ciphertext,"YELLOW SUBMARINE",("0" * 16)) #you can decrypt back
    if back_plaintext != plaintext:
        raise Exception("Couldn't convert to plaintext back.")
    '''
    plaintext = base64.b64decode(open('file_CBC.txt','r').read())
    back_plaintext = CBC_decrypt(plaintext,"YELLOW SUBMARINE",("0" * 16))
    print(back_plaintext)
