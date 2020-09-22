def split_len(m, n) :
    return [m[i :i + n] for i in range(0, len(m), n)]


def enc(m, key) :
    order = {
        val : num for num, val in enumerate(key)
    }
    cipher_text = " "
    for i in sorted(order.keys()) :
        for p in split_len(m, len(key)) :
            try :
                cipher_text += p[order[i]]
            except IndexError :
                continue
    print("Cipher text is: ", cipher_text)


message = "This is an example of transposition cipher"
key = "hack"
enc(message, key)
