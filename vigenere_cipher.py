from string import ascii_uppercase


def enc(message, key) :
    key = key.upper()
    ki = 0
    cipher_text = ''
    for i in message :
        n = ascii_uppercase.find(i.upper())
        if n != -1 :
            n = (n + ascii_uppercase.find(key[ki])) % 26
            if i.isupper() :
                cipher_text += ascii_uppercase[n]
            elif i.islower() :
                cipher_text += ascii_uppercase[n].lower()
            ki += 1
            if ki == len(key) :
                ki = 0
        else :
            cipher_text += i
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text, key) :
    key = key.upper()
    ki = 0
    plain_text = ''
    for i in cipher_text :
        n = ascii_uppercase.find(i.upper())
        if n != -1 :
            n = (n - ascii_uppercase.find(key[ki])) % 26
            if i.isupper() :
                plain_text += ascii_uppercase[n]
            elif i.islower() :
                plain_text += ascii_uppercase[n].lower()
            ki += 1
            if ki == len(key) :
                ki = 0
        else :
            plain_text += i
    print("Plain text is:", plain_text)


message = "This is Vigenere Cipher example"
key = "HELLO"
cipher_text = enc(message, key)
dec(cipher_text, key)
