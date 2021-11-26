def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    di= {alphabet[i] : i for i in range(0,len(alphabet))}
    punctuation = "!@#$%^&*()_+<>?:.,; "
    for c in text:
        if c in punctuation:
            text = text.replace(c, "")
    txt = [di[i] for i in text.upper()]
    l = ""
    if reverse:
        k = [-int(c) for c in str(key)]
    else:
        k = [int(c) for c in str(key)]
    j = 0
    i = 0
    while j < len(text):
        l = l+ caesar(text[j],k[i],alphabet)
        j+=1
        i+=1
        i = i % len(k)
    return l

def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    punctuation = "!@#$%^&*()_+<>?:.,; "
    for c in text:
        if c in punctuation:
            text = text.replace(c, "")
    di= {alphabet[i] : i for i in range(0,len(alphabet))}
    txt = [di[i] for i in text.upper()]
    return "".join([list(di.keys())[(i+ key)%len(alphabet)] for i in txt])

print("Type the text you want to encrypt:")
text = input()
print("Type the encryption key (integer number):")
key = int(input())
enc_text = jarriquez_encryption(text, key)
print(f"Encrypted text: {enc_text}")
print(f"Decrypted back: {jarriquez_encryption(enc_text, key, reverse=True)}")
