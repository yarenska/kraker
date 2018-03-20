import binascii
import StringIO

def PKCS_7(text,block):
    block_size = 16;
    pad_time =  block % block_size
    output = StringIO.StringIO()
    for i in range(0,pad_time):
        output.write(chr(int(format(pad_time, '02x'))))
    
    return text+output.getvalue()


text = "YELLOW SUBMARINE"
print(PKCS_7(text,20))
