import random


def enc(message, key) :
    cipher_text = ''.join(key[i] for i in message)
    print("Cipher text is:", cipher_text)
    return cipher_text


def genkey() :
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'
    shuffled_chars = sorted(chars, key=lambda k : random.random())
    return dict(zip(chars, shuffled_chars))


def dec(cipher_text, key) :
    key_val = {v : k for k, v in key.items()}
    print("Plaintext is: ", ''.join(key_val[i] for i in cipher_text))


message = "This is substitution cipher example1"
key = genkey()
cipher_text = enc(message, key)
dec(cipher_text, key)
