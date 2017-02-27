OPEN_BRACES = '[{('
CLOSED_BRACES = ']})'


def check_brackets(string):
    if len(string) % 2 != 0:
        return False
    if not string:
        return True
    braces = []
    for brace in string:
        if brace in OPEN_BRACES:
            braces.append(brace)
        elif brace in CLOSED_BRACES:
            if not braces:
                return False
            index = OPEN_BRACES.index(braces.pop())
            if CLOSED_BRACES[index] != brace:
                return False
    return not braces
