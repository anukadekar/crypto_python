def enc(message) :
    cipher_text = message[: :-1]
    print("Cipher text is:", cipher_text)
    return cipher_text


def dec(cipher_text) :
    plain_text = cipher_text[: :-1]
    print("Plain text is: ", plain_text)


message = "This is reverse cipher"
cipher_text = enc(message)
dec(cipher_text)
