import binascii
import random


def genkey(p) :
    k = ''
    for i in range(int(p)) :
        t = random.randint(0, 1)
        k += str(t)
    return k


def xor(f1, f2) :
    t = ''
    for i in range(len(f1)) :
        if f1[i] == f2[i] :
            t += '0'
        else :
            t += '1'
    return t


def enc_dec(message) :
    ascii_val = [ord(i) for i in message]
    bin_format = [format(j, '08b') for j in ascii_val]
    bin_format = ''.join(bin_format)

    n = int(len(bin_format) // 2)
    l1 = bin_format[0 :n]
    r1 = bin_format[n : :]
    m = len(r1)

    k1 = genkey(m)
    k2 = genkey(m)

    f1 = xor(r1, k1)
    r2 = xor(f1, l1)
    l2 = r1

    f2 = xor(r2, k2)
    r3 = xor(f2, l2)
    l3 = r2

    data = l3 + r3
    str = ''
    for i in range(0, len(data), 7) :
        tdata = data[i :i + 7]
        ddata = int(tdata, 2)
        str += chr(ddata)

    print("Cipher text is: ", str)

    l4 = l3
    r4 = r3

    f3 = xor(l4, k2)
    l5 = xor(r4, f3)
    r5 = l4

    f4 = xor(l5, k1)
    l6 = xor(r5, f4)
    r6 = l5

    plain_text = int((l6 + r6), 2)
    plain_text = binascii.unhexlify('%x' % plain_text)
    print("Plain text is:", plain_text)


message = "This is Feistel cipher"
enc_dec(message)
