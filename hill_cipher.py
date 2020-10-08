from string import ascii_letters


def genkey(message) :
    l = len(message)
    key = ascii_letters * len(message)
    keymatrix = [[0] * l for _ in range(l)]
    k = 0
    for i in range(l) :
        for j in range(l) :
            keymatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keymatrix


def enc(message, keymatrix) :
    l = len(message)
    mvector = [[0] * l for i in range(l)]
    for i in range(l) :
        mvector[i][0] = ord(message[i]) % 65

    c = [[0] * l for i in range(l)]
    for i in range(l) :
        for j in range(1) :
            c[i][j] = 0
            for x in range(l) :
                c[i][j] += keymatrix[i][x] * mvector[x][j]
            c[i][j] = c[i][j] % 26

    cipher_text = []
    for i in range(l) :
        cipher_text.append(chr(c[i][0] + 65))
    return (''.join(cipher_text))


message = "THIS IS HILL CIPHER EXAMPLE"
keym = genkey(message)
cipher_text = enc(message, keym)
print("Cipher text is: ",cipher_text)
