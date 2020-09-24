def enc(message, key) :
    ctext =""
    for c in message:
        if c.isdigit() and ord(c) != 32 :
            ctext += chr((ord(c) - 48 * key) % 10 + 48)
        elif c.isupper() and ord(c) !=32:
            ctext += chr((ord(c) - 65 * key) % 26 + 65)
        elif c.islower() and ord(c) !=32:
            ctext += chr((ord(c) - 97 * key) % 26 + 97)
        elif ord(c) == 32:
            ctext += " "
    print("Cipher text is:", ctext)

message = "This is multiplicative cipher"
key = 71678999
enc(message, key)
