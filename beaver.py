#Recursive implementation of beaver code from mysterytwisterc3.org

def beaver_code(plaintext, left, right):
    if(len(plaintext) == 1 or len(plaintext) == 2):
        return plaintext
    else:
        for i in range(len(plaintext)):
            if(i % 2 == 0):
                left += plaintext[i]
            else:
                right += plaintext[i]
    return beaver_code(left, "", "") + beaver_code(right, "", "")
    

if __name__ == '__main__':
    plaintext = "I like chocolate and ice cream.."
    plaintext = plaintext.replace(" ", "")
    left = ""
    right = ""

    '''
    beaver_code is for both encryption and decryption.
    After many trials you can find your plaintext back.
    '''
    for i in range(len(plaintext)):
        plaintext = beaver_code(plaintext, left, right)
        print(plaintext)
