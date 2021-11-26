from random import seed, shuffle
def disc_generator(alphabet):
    l = list(alphabet)
    shuffle(l)
    return "".join(l)
clear_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Number of new alphabets:')
n = int(input())
print("Shift for Caesar:")
step = int(input())
seed(42)
discs = [disc_generator(clear_alphabet) for i in range(n)]

def jefferson_encryption(text, discs, step, reverse=False):
    punctuation = "!@#$%^&*()_+<>?:.,; "
    for c in text:
        if c in punctuation:
            text = text.replace(c, "")
    ans = ""
    j = 0
    for c in text:
        ans = ans + caesar(c, step, discs[j], reverse)
        j += 1
        j = j % len(discs)
    return ans


def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse = False):
    if reverse:
        key *= -1
    di= {alphabet[i] : i for i in range(0,len(alphabet))}
    txt = [di[i] for i in text.upper()]
    return "".join([list(di.keys())[(i + key)%len(alphabet)] for i in txt])

print("Type the text you want to encrypt:")
text = input()
text_enc = jefferson_encryption(text, discs, step)
print(f'Encrypted text: {text_enc}')
print(f'Decrypted back: {jefferson_encryption(text_enc, discs, step, True)}')
