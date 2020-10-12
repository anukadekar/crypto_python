from string import ascii_uppercase
import random


def genmsg(message) :
    str = ''
    for i in message :
        if i == ' ' :
            str += ''
        else :
            str += i
    return str


def genkey(n) :
    key = ''
    stru = ascii_uppercase
    key += ''.join(random.choice(stru) for _ in range(n))
    return key


def enc(message, key) :
    message = message.upper()
    d = {}
    stru = ascii_uppercase
    v = 0
    for i in stru :
        d[i] = v
        v += 1
    l = []
    l1 = []
    ctv = []
    for i in message :
        l.append(d[i])
    for k in key :
        l1.append(d[k])
    for i in range(len(message)) :
        ct = l[i] + l1[i]
        if ct < 26 :
            ctv.append(ct)
        else :
            ctv.append(ct - 26)
    cipher_text = ''
    for i in ctv :
        cipher_text += list(d.keys())[list(d.values()).index(i)]
    print("Cipher text is:", cipher_text)
    return cipher_text


message = "This is Vernam Cipher example"
msg = genmsg(message)
key = genkey(len(msg))
cipher_text = enc(msg, key)
