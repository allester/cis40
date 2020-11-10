"""
Lab 3 - fibonacci.py - De Anza  CIS D040 - Allester Ramayrat
"""

def fibonacci(number):

    num1 = 0
    num2 = 1

    if number > 0:
        print(num1)

    if number > 1:
        print(num2)

    for i in range(number-2):

        num3 = num1 + num2

        print(num3)

        num1 = num2
        num2 = num3

fibonacci(12)