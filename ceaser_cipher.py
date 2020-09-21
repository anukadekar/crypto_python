def enc(message, s) :
    cipher_text = ""
    for i in range(len(message)) :
        c = message[i]
        if c.isupper() and ord(c) != 32 :
            cipher_text += chr((ord(c) + s - 65) % 26 + 65)
        elif c.islower() and ord(c) != 32 :
            cipher_text += chr((ord(c) + s - 97) % 26 + 97)
        elif ord(c) == 32 :
            cipher_text += " "
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text, s) :
    plain_text = ""
    for i in range(len(message)) :
        c = cipher_text[i]
        if c.isupper() and ord(c) != 32 :
            plain_text += chr((ord(c) - s - 65) % 26 + 65)
        elif c.islower() and ord(c) != 32 :
            plain_text += chr((ord(c) - s - 97) % 26 + 97)
        elif ord(c) == 32 :
            plain_text += " "
    print("Plain text is:", plain_text)


def hack_brute_force(cipher_text) :
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for k in range(len(letters)) :
        t = ' '
        for j in cipher_text :
            if j in letters :
                n = letters.find(j)
                n = n - k
                if n < 0 :
                    n += len(letters)
                t += letters[n]
            else :
                t += letters[n]
        print(k, t)


message = "This is ceaser cipher"
shift_value = 4
cipher_text = enc(message, shift_value)
dec(cipher_text, shift_value)
hack_brute_force(cipher_text)
