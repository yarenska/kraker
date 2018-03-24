def decrypt_letter(key,ciphertext):
    temp1 = ""
    temp2 = ""
    plaintext = ""
    print(len(ciphertext))
    for i in xrange(0,len(ciphertext),2):
        try:
            temp1 = ciphertext[i+1]
            temp2 = ciphertext[i]
            plaintext = plaintext+temp1+temp2
        except:
            temp2 = ciphertext[i]
            plaintext = plaintext+temp2
            break
    return plaintext

if __name__ == '__main__':
    ciphertext = open("mtc3-esslinger-15-cipher-en.txt", "r").read().replace(" ","")
    print(decrypt_letter(21,ciphertext))
