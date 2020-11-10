"""
Reading Quiz 5B Question 3 - bette.py - De Anza  CIS D040 - Allester Ramayrat
"""

docBette = open("bette.txt")

movieDict = {}
for line in docBette:
    line = line.strip()
    lineLen = len(line)
    year = ""
    for i in range(4):
        year += line[lineLen-5+i]

    year = int(year)

    if year not in movieDict:
        movieDict[year] = ["*"]
    else:
        movieDict[year].append("*")

for key in sorted(movieDict):
    print(key, ":", "".join(movieDict[key]))
