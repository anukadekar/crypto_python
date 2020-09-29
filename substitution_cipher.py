import random
from random import shuffle
from string import ascii_letters


def enc(message, key) :
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ""
    for i in message :
        if i.upper() in letters :
            ind = letters.find(i.upper())
            if i.isupper() :
                cipher_text += key[ind].upper()
            elif i.islower() :
                cipher_text += key[ind].lower()
        else :
            cipher_text += i
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text, key) :
    letters = ascii_letters
    plain_text = ""
    for i in cipher_text :
        if i.upper() in key :
            ind = key.find(i.upper())
            if i.isupper() :
                plain_text += letters[ind].upper()
            elif i.islower() :
                plain_text += letters[ind].lower()
        else :
            plain_text += i
    print("Plain text is:", plain_text)


def getrandomletters() :
    l=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(l)
    return ''.join(l)


message = "This is substitution cipher example"
key = getrandomletters()
cipher_text = enc(message, key)
dec(cipher_text, key)
