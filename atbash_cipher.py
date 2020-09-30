from string import ascii_uppercase


def genkey() :
    k = ascii_uppercase
    l = k[::-1]
    return (dict(zip(k, l)))


def enc(message, k) :
    cipher_text = ''
    for i in message :
        if i != ' ' :
            cipher_text += k.get(i.upper(), i)
        else :
            cipher_text += ' '
    print(cipher_text)
    return cipher_text


def dec(cipher_text, k) :
    plain_text = ''
    d = {}
    for key, val in k.items() :
        d[val] = key

    for i in cipher_text :
        if i != ' ' :
            plain_text += d.get(i, i)
        else :
            plain_text += ' '
    print(plain_text)


message = "THIS IS ATBASH CIPHER"
k = genkey()
cipher_text = enc(message, k)
dec(cipher_text, k)
