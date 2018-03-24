import binascii
import StringIO

def PKCS_7(text,block):
    pad_time =  block % len(text)
    output = StringIO.StringIO()
    for i in range(0,pad_time):
        output.write(chr(int(format(pad_time, '02x'))))
    
    return text+output.getvalue()


text = "YELLOW SUBMARINE"
print(PKCS_7(text,20))
