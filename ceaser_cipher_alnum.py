def enc(str, s) :
    cipher_text = " "
    for i in range(len(str)) :
        c = str[i]
        if c.isdigit() and ord(c) != 32 :
            cipher_text += chr((ord(c) + s - 48) % 10 + 48)
        elif c.isupper() and ord(c) != 32 :
            cipher_text += chr((ord(c) + s - 65) % 26 + 65)
        elif c.islower() and ord(c) != 32 :
            cipher_text += chr((ord(c) + s - 97) % 26 + 97)
        elif ord(c) == 32 :
            cipher_text += " "
    print("Cipher text is:", cipher_text)


message = "This is an example of ceaser cipher application 123"
shift_value = 4
enc(message, shift_value)
