bottle_template = (
    "{this} bottles of beer on the wall, {this} bottles of beer.\n"
    "Take one down and pass it around, "
    "{next} bottle{plural} of beer on the wall.\n"
)
one_template = (
    "1 bottle of beer on the wall, 1 bottle of beer.\n"
    "Take it down and pass it around, "
    "no more bottles of beer on the wall.\n"
)
zero_template = (
    "No more bottles of beer on the wall, no more bottles of beer.\n"
    "Go to the store and buy some more, "
    "99 bottles of beer on the wall.\n"
)


def verse(number):
    if number > 1:
        plural = '' if number <= 2 else 's'
        return bottle_template.format(this=number, next=number - 1, plural=plural)
    elif number == 1:
        return one_template
    else:
        return zero_template


def song(start_verse, stop_verse=0):
    result = '\n'.join([verse(number)
                        for number in range(start_verse, stop_verse - 1, -1)]
                       )
    return result + '\n'
