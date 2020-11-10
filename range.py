"""
FINAL EXAM Q 11 - range.py - De Anza  CIS D040 - Allester Ramayrat
"""

def grades(docGrades):
    gradeList = []

    for num in docGrades:
        num = int(num.strip())
        gradeList.append(num)
    lenList = len(gradeList)
    gradeList.sort()
    print("Range of grades is :", gradeList[-1] - gradeList[0])

    total = 0
    for num in gradeList:
        total += num
    mean = total / lenList
    print("Mean grade is :", mean)

    for i in range(lenList):
        gradeList[i] = gradeList[i]
    gradeList.sort()

    if len(gradeList) % 2 != 0: # is odd
        median = gradeList[int(lenList - 1) // 2]
    else: # is even
        median = (gradeList[lenList // 2] + gradeList[lenList // 2 - 1]) / 2
    print("Median grade is :", median)

    gradeFreq = {}
    for grade in gradeList:
        if grade not in gradeFreq:
            gradeFreq[grade] = 1
        else:
            gradeFreq[grade] += 1

    maxFreq = 0
    for grade in gradeFreq:
        if gradeFreq[grade] > maxFreq:
            maxFreq = gradeFreq[grade]

    print("Mode grade(s) : ", end = "")
    for grade in gradeFreq:
        if gradeFreq[grade] == maxFreq:
            print(str(grade) + " " , end = "")
    print("occurred", maxFreq, "time(s) each\n")

docGrades = open('numbers-even.txt')
grades(docGrades)

docGrades = open('numbers-odd.txt')
grades(docGrades)