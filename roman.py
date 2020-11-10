"""
Lab 4 - roman.py - De Anza  CIS D040 - Allester Ramayrat
"""

def conversion(digit, char1, char2, char3):

    if digit == 9:

        string = char1 + char3

    if digit < 9:

        string = char2 + char1 * (digit - 5)

    if digit == 4:

        string = char1 + char2

    if digit < 4:

        string = char1 * digit

    return string

def thousands(num):

    digit = num % 10000 // 1000

    return conversion(digit, "M", "", "")

def hundreds(num):

    digit = num % 1000 // 100

    return conversion(digit, "C", "D", "M")

def tens(num):

    digit = num % 100 // 10

    return conversion(digit, "X", "L", "C")

def ones(num):

    digit = num % 10

    return conversion(digit, "I", "V", "X")

def roman(num):

    roman = thousands(num) + hundreds(num) + tens(num) + ones(num)

    print(num, "as Roman Numerals is " + roman)

print("Welcome to Arabic to Roman Numeral Converter!")
print("Enter four-digit numbers. To end type \"Done\".")

while True:

    userinput = input()

    if userinput == "done" or userinput == "Done":

        break

    else:
        roman(int(userinput))
