for i in range(100):

    num = i + 1

    not_divisible = True

    for j in range(8):

        if num % (j + 2) == 0:

            not_divisible = False

    if not_divisible:
        print(num, "not divisible by any digit other than 1")