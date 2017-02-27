def test_params(old, num, new):
    if not (old >= 2 and new >= 2):
        return False
    if num and max(num) >= old:
        return False
    # try:
    # 	if max(num) >= old:
    # 		return False
    # except ValueError:
    # 	pass
    for val in num:
        if val < 0:
            return False
    return True


def to_decimal(old, nums):
    expo = len(nums) - 1
    total = 0
    for index, number in enumerate(nums):
        total += number * old ** (expo)
        expo -= 1
    return list(map(int, list(str(total))))


def from_decimal(base, nums):
    lst = []
    number = int(''.join(map(str, nums)))
    while number > 0:
        number, rem = divmod(number, base)
        lst.append(rem)
    return list(reversed(lst))


def rebase(old_base, num, new_base):
    if not test_params(old_base, num, new_base):
        raise ValueError
    if num == []:
        lst = []
    elif old_base == 10:
        lst = from_decimal(new_base, num)
    elif new_base == 10:
        lst = to_decimal(old_base, num)
    else:
        lst = from_decimal(new_base, to_decimal(old_base, num))
    return lst
