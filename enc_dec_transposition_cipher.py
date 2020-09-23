import math


def enc(message, key) :
    ciphertext = [''] * key
    for i in range(key) :
        p = i
        while p < len(message) :
            ciphertext[i] += message[p]
            p += key
    print("Cipher text is:", ''.join(ciphertext))
    return ''.join(ciphertext)


def dec(ciphetext, key) :
    ncol = math.ceil(len(ciphertext) / key)
    nrow = key
    col = 0
    row = 0
    nsb = (ncol * nrow) - len(ciphertext)
    ptext = ['']*ncol
    for i in ciphertext :
        ptext[col] += i
        col += 1
        if col == ncol or (col == ncol - 1 and row >= nrow - nsb) :
            col = 0
            row += 1
    print("Original text is:",''.join(ptext))


message = "This is an example for Transposition Cipher"
key = 5
ciphertext = enc(message, key)
dec(ciphertext, key)
