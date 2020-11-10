def factorial(num):
    fac = 1

    for i in range(num):

        fac = fac * (i + 1)
    print(fac)

arg = int(input("Input a number to get its factorial: "))

factorial(arg)

import math
print(math.factorial(arg))