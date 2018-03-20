from base64 import b64decode
from Crypto.Cipher import AES

f = open("fileAES128.txt","r")
text = b64decode(f.read())
key = "YELLOW SUBMARINE"
decryptor = AES.new(key, AES.MODE_ECB);
plaintext = decryptor.decrypt(text)
print(plaintext)


