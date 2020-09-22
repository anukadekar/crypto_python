def enc(s1, s2, s) :
    ctext1 = " "
    for i in range(len(s1)) :
        c = s1[i]
        if c.isdigit() and ord(c) != 32 :
            ctext1 += chr((ord(c) - 48 + s) % 10 + 48)
        elif c.isupper() and ord(c) !=32:
            ctext1 += chr((ord(c) - 65 + s) % 26 + 65)
        elif c.islower() and ord(c) !=32:
            ctext1 += chr((ord(c) - 97 + s) % 26 + 97)
        elif ord(c) == 32:
            ctext1 += " "
    ctext2 = " "
    for i in range(len(s2)):
        if i%2 == 0:
            c = s2[i]
            if c.isdigit() and ord(c) != 32 :
                ctext2 += chr((ord(c) - 48 + s) % 10 + 48)
            elif c.isupper() and ord(c) != 32 :
                ctext2 += chr((ord(c) - 65 + s) % 26 + 65)
            elif c.islower() and ord(c) != 32 :
                ctext2 += chr((ord(c) - 97 + s) % 26 + 97)
            elif ord(c) == 32 :
                ctext2 += " "
        else:
            ctext2 += s2[i]
    print("Cipher text is:", ctext1+ctext2)

message1 = "This is a example of ceaser cipher 456"
message2 = "This is encrypted at alternate characters 123"
shift_value = 4
enc(message1, message2,shift_value)
