def enc(message, k1, k2) :
    ctext = ""
    for c in message :
        if c.isupper() and ord(c) != 32 :
            ctext += chr((k1 * (ord(c) - 65) + k2) % 26 + 65)
        elif c.islower() and ord(c) != 32 :
            ctext += chr((k1 * (ord(c) - 97) + k2) % 26 + 97)
        elif ord(c) == 32 :
            ctext += " "
    print("Cipher text is:", ctext)
    return ctext


def modinv(a, m) :
    x = 0
    while (x <= m) :
        if (a * x) % m == 1 :
            return x
        x += 1


def dec(ctext, k1, k2) :
    ptext = ""
    for c in ctext :
        if c.isupper() and ord(c) != 32 :
            ptext += chr(((modinv(k1, 26) * (ord(c) - 65 - k2)) % 26) + 65)
        elif c.islower() and ord(c) != 32 :
            ptext += chr(((modinv(k1, 26) * (ord(c) - 97 - k2)) % 26) + 97)
        elif ord(c) == 32 :
            ptext += " "
    print("Plain text is:", ptext)


message = "This is affine cipher"
k1 = 17
k2 = 20
ctext = enc(message, k1, k2)
dec(ctext, k1, k2)