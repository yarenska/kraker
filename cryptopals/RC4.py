import sys

def PRGA(S):
    #Stream Generation
    i = 0
    j = 0
    while True:
        i = (i + 1) % 32
        j = (j + S[i]) % 32
        S[i], S[j] = S[j], S[i] 

        K = S[(S[i] + S[j]) % 32]
        yield K


def KSA(key):
    S = []
    T = []

    #Initialization
    for i in range(0,32):
        S.append(i)
        T.append(key[i % len(key)])
    
    #Initial Permutation of S
    j = 0
    for i  in range(0,32):
        j = (j + S[i] + ord(T[i])) % 32
        S[i],S[j] = S[j],S[i]

    return S

def RC4(key):
    S = KSA(key);
    return PRGA(S);
    
if __name__ == '__main__':
    #Example
    key = "KEY"
    plaintext = "hello"
    #c = 7E75617668

    #key = "KEY"
    #plaintext = "there"
    #c1 = 6278686862
    keystream = RC4(key)

    for c in plaintext:
        sys.stdout.write("%02X" % (ord(c) ^ keystream.next()))
    print

    
