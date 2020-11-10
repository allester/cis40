"""
FINAL EXAM Q 12 - bette_report.py - De Anza  CIS D040 - Allester Ramayrat
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
        movieDict[year] = [line[0:lineLen-7]]
    else:
        movieDict[year].append(line[0:lineLen-7])

for key in sorted(movieDict):
    print(key, ":\n", "\n".join(movieDict[key]), sep = "", end = "\n\n")
