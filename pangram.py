"""
Reading Quiz 5A Question 3 - pangram.py - De Anza  CIS D040 - Allester Ramayrat
"""

userInput = input("Enter a sentence for pangram-checking: ")
listInput = list(userInput.lower())
letterCount = list("abcdefghijklmnopqrstuvwxyz")

for char in listInput:
    if char in letterCount:
        letterCount.remove(char)

if letterCount == []:
    print("\"", userInput, "\" is a pangram", sep = "")

else:
    print("\"", userInput, "\" is NOT a pangram", sep = "")