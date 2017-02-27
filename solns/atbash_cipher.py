import string
import re

CIPHERTEXT = 'zyxwvutsrqponmlkjihgfedcba' + string.digits
PLAINTEXT = string.ascii_lowercase + string.digits


def encode(str_):
    str_ = re.sub('\W', '', str_).lower()
    return_str = ''
    count = 1
    for letter in str_:
        return_str += CIPHERTEXT[PLAINTEXT.index(letter)]  # letter if letter.isdigit() else
        if count == 5:
            return_str += ' '
            count = 0
        count += 1
    return ' '.join(return_str.split())


def decode(cipher):
    cipher = re.sub('\W', '', cipher)
    return_str = ''
    for letter in cipher:
        return_str += PLAINTEXT[CIPHERTEXT.index(letter)]
    return return_str
