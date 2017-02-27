import math
import re


def encode(msg):
    if not msg:
        return msg
    msg = re.sub('[\W\s]', '', msg).lower()
    length = len(msg)
    col = math.ceil(length ** 0.5)
    row = math.ceil(length / col)
    lst = [[] for i in range(col)]

    for index, letter in enumerate(msg):
        lst[index % col].append(letter)

    return ' '.join([''.join(l_) for l_ in lst])
