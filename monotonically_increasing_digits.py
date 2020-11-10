"""
Practice Final Exam Question 4 - monotonically-increasing-digits.py - De Anza - CIS D040 - Allester Ramayrat
"""

digits = list(input("Enter string of digits: "))

counter = -1
isMID = True
for i in range(len(digits)):
    currDigit = int(digits[i])
    if currDigit > counter:
        counter = currDigit
    else:
        isMID = False
if isMID:
    print("".join(digits), "is composed of monotonically increasing digits")
else:
    print("".join(digits), "is NOT composed of monotonically increasing digits")

