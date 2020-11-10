"""
Lab 6 - jumble.py - De Anza  CIS D040 - Allester Ramayrat
"""

docWords = open('words.txt')
jumble = list(input("Enter a jumbled word of any length: ").lower())
jumble.sort()

for line in docWords:
    currWord = list(line.strip())
    currWord.sort()
    if currWord == jumble:
        print(line.strip(), end = " ")

