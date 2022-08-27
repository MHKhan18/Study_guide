def is_self_describing(num: str) -> int:

    num_count = {}

    for digit in num:  # digit is character
        num_count[digit] = num_count.get(digit, 0) + 1

    for pos, value in enumerate(num):
        pos = str(pos)

        if int(value) > 0 and not (pos in num_count):
            return 1
        if int(value) == 0 and (pos in num_count):
            return 1
        if int(value) == num_count.get(pos, 0):
            continue

        if int(value) != num_count.get(pos, 0):
            return 1

    return 0


print(is_self_describing("2020"))
