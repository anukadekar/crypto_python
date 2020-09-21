from gi.module import maketrans


def enc(message) :
    rot13trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    cipher_text = message.translate(rot13trans)
    print(cipher_text)
    return cipher_text

def dec(message):
    rot13trans = maketrans('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    plain_text = message.translate(rot13trans)
    print(plain_text)


message = "This is rot13 cipher"
cipher_text = enc(message)
dec(cipher_text)
