import random
from string import ascii_lowercase, ascii_uppercase


def genkey() :
    strl = ascii_lowercase
    stru = ascii_uppercase
    d = {}
    for i in stru :
        d[i] = ''.join(random.choice(strl) for i in range(5))
    return d


def enc(message, key) :
    cipher_text = ''
    for i in message.upper() :
        if i == ' ' :
            cipher_text += ' '
        else :
            cipher_text += key[i]
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text, key) :
    plain_text = ''
    i = 0
    while 1 :
        if i < len(cipher_text) - 4 :
            str = cipher_text[i :i + 5]
            if str[0] == ' ' :
                plain_text += ' '
                i += 1
            else :
                plain_text += list(key.keys())[list(key.values()).index(str)]
                i += 5
        else :
            break
    print("Plain text is:", plain_text)


message = "This is baconian cipher"
key = genkey()
cipher_text = enc(message, key)
dec(cipher_text, key)
