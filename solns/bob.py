#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = what.strip()
    if not what:
        response = "Fine. Be that way!"
    elif what.endswith('?') and not what.isupper():
        response = "Sure."
    elif what.isupper():
        response = "Whoa, chill out!"
    else:
        response = "Whatever."
    return response
