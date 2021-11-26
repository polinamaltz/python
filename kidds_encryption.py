def kidds_encryption(text, reverse=False):
    a1 = "ethosnairfdlmbyguvcp"
    a2 = "8;4‡)*56(1†092:3?¶-."
    if reverse:
        txt = "".join([c for c in text.lower() if c in a2])
        return "".join([a1[a2.index(c)] for c in txt])
    else:
        txt = "".join([c for c in text.lower() if c in a1])
        return "".join([a2[a1.index(c)] for c in txt])

text = input()
print(f'Encryption:      {kidds_encryption(text)}\nDecryption back: {kidds_encryption(kidds_encryption(text), True)}')
