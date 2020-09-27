from string import ascii_letters, digits
from random import shuffle


def monoalphabetic_cipher(pool=None) :
    if pool is None :
        pool = ascii_letters + digits
    op = list(pool)
    sp = list(pool)
    shuffle(sp)
    return dict(zip(op, sp))


def enc_monoalpha_cipher(message, cipher) :
    l = []
    for i in message :
        l.append(cipher.get(i, i))
    return "".join(l)


def inv_monoalpha_cipher(cipher) :
    d = {}
    for k, v in cipher.items() :
        d[v] = k
    return d


def dec_monoalpha_cipher(enc_message, cipher) :
    return enc_monoalpha_cipher(enc_message, inv_monoalpha_cipher(cipher))


message = "This is monoalphabetic cipher"
c = monoalphabetic_cipher()
enc_message = enc_monoalpha_cipher(message, c)
dec_message = dec_monoalpha_cipher(enc_message, c)
print("Cipher text is:", enc_message)
print("Plain text is:", dec_message)
