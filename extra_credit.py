def while_downwards(starting_num, by_num):

    while starting_num > 0:

        if starting_num % 2 == 0:

            print(str(starting_num).rjust(8))

        starting_num = starting_num - by_num

while_downwards(1974,26)