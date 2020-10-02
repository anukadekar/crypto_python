from string import ascii_uppercase


def genkey(key) :
    str = ascii_uppercase
    str1 = ''
    key = key.replace(' ', '')
    k = ''
    for j in key :
        if j not in k :
            k += j
    for i in str :
        if i not in key.upper() :
            str1 += i
    key = k.upper() + str1
    return key


def enc(message, key) :
    cipher_text = ''
    for i in message :
        if i.isupper() :
            ind = ascii_uppercase.find(i.upper())
            cipher_text += key[ind].upper()
        elif i.islower() :
            ind = ascii_uppercase.find(i.upper())
            cipher_text += key[ind].lower()
        else :
            cipher_text += i
    print("Cipher text: ", cipher_text)
    return cipher_text


def dec(cipher_text, key) :
    plain_text = ''
    for i in cipher_text :
        if i.isupper() :
            ind = key.find(i.upper())
            plain_text += ascii_uppercase[ind].upper()
        elif i.islower() :
            ind = key.find(i.upper())
            plain_text += ascii_uppercase[ind].lower()
        else :
            plain_text += i
    print("Plain text: ", plain_text)



message = "This is keyword cipher example"
key = "secret"
k = genkey(key)
cipher_text = enc(message, k)
dec(cipher_text, k)
