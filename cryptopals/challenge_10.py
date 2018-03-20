from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

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
    plaintext = "I like chocolate and ice cream.." #i made that up to see whether my algorithm works or not you will do
                                                   #plaintext = base64.b64decode(open('10.txt','r').read())
    ciphertext = CBC_encrypt(plaintext,"YELLOW SUBMARINE",("0" * 16))
    back_plaintext = CBC_decrypt(ciphertext,"YELLOW SUBMARINE",("0" * 16))
    
    if(back_plaintext != plaintext):
        raise Exception("Couldn't go back to plaintext..")
    else:
        print("Plaintext: " + plaintext)
        print("Encrypted: " + ciphertext)
        print("Decrypted: " + back_plaintext)
