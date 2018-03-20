from Crypto.Util.strxor import strxor_c

#Frequency mapping is constructed according to the data from:
#https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
#http://letterfrequency.org/ part: "Computer QWERTY Keyboard Key Frequency"

letter_freq = {' ': 12.42,'e': 12.02, 't': 9.10,
               'a': 8.12, 'o': 7.68, 'i': 7.31,
               'n': 6.95, 's': 6.28, 'r': 6.02,
               'h': 5.92, 'd': 4.32, 'l': 3.98,
               'u': 2.88, 'c': 2.71, 'm':2.61,
               'f': 2.30, 'y': 2.11, 'w': 2.09,
               'g': 2.03, 'p': 1.82, 'b': 1.49,
               'v': 1.11, 'k': 0.69, 'x': 0.17,
               'q': 0.11, 'j': 0.1, 'z': 0.07}

def score(t):
    score = 0
    for i in range(len(t)):
        try:
            score += letter_freq[t[i]]
        except:
            break
    return score
   

def detect_key_decrypt(text):
    w, h = 34, 256
    results = [[" " for x in range(w)] for y in range(h)] 
    for i in range(0,256):
        results[i] = (strxor_c(text,i).lower())

    max = 0
    sentence = []
    for i in range(0,h):
        if(score(results[i]) > max):
            max = score(results[i])
            sentence = results[i]
    return sentence
   
if __name__ == '__main__':
    hex_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(detect_key_decrypt(hex_text.decode('hex')))
