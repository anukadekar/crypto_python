def enc(message, key) :
    cipher_text = ''
    for i in range(len(message)) :
        cipher_text += (chr(ord(key) ^ ord(message[i])))
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text, key) :
    plain_text = ''
    for i in range(len(cipher_text)) :
        plain_text += chr(ord(key) ^ ord(cipher_text[i]))
    print("Plain text is:", plain_text)


message = "This is XOR cipher"
key = "A"
cipher_text = enc(message, key)
dec(cipher_text, key)
