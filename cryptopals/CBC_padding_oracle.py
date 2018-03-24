from challenge_15 import *
from challenge_10 import *
from challenge_9 import PKCS_7
import random
import os

string_field = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
                "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
                "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
                "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
                "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
                "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
                "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
                "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
                "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
                "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"
                ]

def randbytes(n):
    return os.urandom(16)

def closest_dividend(n):
    i = 0
    while(i < n):
        i = i+16
    return i
    
def some_more_stuff(ciphertext,key,iv):
    plaintext = CBC_decrypt(ciphertext,key,iv)
    if(len(plaintext)%16 == 0):
        print("Everything ok.")
    else:
        unpadded = isValidPKCS_7(plaintext)
        print(unpadded)

def do_stuff():
    key = randbytes(16)
    text = string_field[random.randint(0,9)]
    print(len(text))
    if(len(text) % 16 != 0):
        n = closest_dividend(len(text))
    else:
        n = 16
    padded_text = PKCS_7(text,n)
    print(padded_text)
    iv = ("0" * 16)
    ciphertext = CBC_encrypt(padded_text,key,iv)
    return (ciphertext,key,iv)
    
    
if __name__ == '__main__':
    ciphertext,key,iv = do_stuff()
    some_more_stuff(ciphertext,key,iv)

