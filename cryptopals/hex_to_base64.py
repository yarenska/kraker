from binascii import unhexlify,b2a_base64

message = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bin_message = unhexlify(message)
cipher_message = b2a_base64(bin_message)
print(cipher_message)
