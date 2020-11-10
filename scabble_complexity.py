"""
Practice Final Exam Question 3- scrabble_complexity.py - De Anza  CIS D040 - Allester Ramayrat
"""

letter_points = {'A':1, 'B':3, 'C':3,  'D':2, 'E':1, 'F':4, 'G':2,
                 'H':4, 'I':1, 'J':8,  'K':5, 'L':1, 'M':3, 'N':1,
                 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
                 'V':4, 'W':4, 'X':8,  'Y':4, 'Z':10}
docWords = open("words.txt")

pointsDict = {}
for line in docWords:
    line = line.strip().upper()
    currPoints = 0
    for char in line:
        currPoints += letter_points[char]

    if currPoints not in pointsDict:
        pointsDict[currPoints] = [line.lower()]
    else:
        pointsDict[currPoints].append(line.lower())
maxPoints = 0
for key in pointsDict:
    if key > maxPoints:
        maxPoints = key

print(pointsDict[key], ":", key, "points")