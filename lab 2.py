"""
Lab 2 - De Anza CIS 40 - Allester Ramayrat
"""

### 1 ###
print('powers')


def powers(num):
    print(num ** 0)
    print(num ** 1)
    print(num ** 2)
    print(num ** 3)
    print(num ** 4)
    print(num ** 5)
    print(num ** 6)
    print(num ** 7)
    print(num ** 8)
    print(num ** 9)
    print(num ** 10)
    print()


powers(2)
powers(3)
powers(10)

### 2 ###
print('palindrome')


def palindrome(s1, s2, s3, s4, s5):
    print(s1, s2, s3, s4, s5)
    print(s5, s4, s3, s2, s1)
    print()


palindrome('l', 'e', 'v', 'e', 'l')
palindrome('r', 'e', 'f', 'e', 'r')
palindrome('s', 'y', 'r', 'u', 'p')

### 3 ###
print('miles_converter')


def miles_converter(miles):
    print(miles, 'miles =', (miles * 1760), 'yards,', (miles * 5280), 'feet,', (miles * 63360), 'inches')


miles_converter(3.4)
