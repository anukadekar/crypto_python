import numpy
import math
from sympy import Matrix


def genkey(keystr) :
    l = []
    for i in keystr :
        l.append(ord(i) % 65)
    n = math.sqrt(len(l))
    if not n.is_integer() :
        print("Matrix should be a square matrix..Enter valid key value")
        exit(0)
    l = numpy.array([l])
    km = l.reshape(int(n), int(n))
    if numpy.linalg.det(km) == 0 :
        print("Matrix must have an inverse")
        exit(0)
    return km


def genmsgmatrix(message, km) :
    l = []
    if len(message) % km.shape[0] != 0 :
        for i in range(len(message)) :
            message += message[i]
            if len(message) % km.shape[0] == 0 :
                break
    for i in message :
        l.append(ord(i) % 65)
    l = numpy.array([l])
    l.resize(int(len(message) / km.shape[0]), km.shape[0])
    return l


def enc(msg, keym) :
    enc = numpy.matmul(msg, keym)
    enc = numpy.remainder(enc, 26)
    ct = enc.ravel()
    cipher_text = ''
    for i in ct :
        cipher_text += chr(i + 65)
    print("Cipher text is:", cipher_text)
    return enc


def dec(cipher_text, keym) :
    inv = Matrix(keym).inv_mod(26)
    inv = numpy.array(inv)
    inv = inv.astype(float)
    dec = numpy.matmul(cipher_text, inv)
    dec = numpy.remainder(dec, 26).flatten()
    dec = dec.reshape(len(dec), 1)
    plain_text = ''
    for i in dec :
        plain_text += chr(int(i) + 65)
    print("Plain text is: ", plain_text)


message = "THIS IS HILL CIPHER EXAMPLE"
keystr = "GYBNQKURQ"
keym = genkey(keystr)
msg = genmsgmatrix(message, keym)
cipher_text = enc(msg, keym)
dec(cipher_text, keym)
