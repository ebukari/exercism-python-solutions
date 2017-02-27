import re


def abbreviate(phrase):
    letters = []
    re_str = '\s(\w)|^(\w)|\W(\w)|[a-z]([A-Z])'
    matches = re.findall(re_str, phrase)
    for match_tup in matches:
        for let in match_tup:
            letters.append(let.strip().upper())
    return ''.join(letters)
