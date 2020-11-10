"""
Lab 7 - word_count.py - De Anza  CIS D040 - Allester Ramayrat
"""

def wordCount(docWords):
    dict = {}
    for line in docWords:
        line = line.strip()
        for currChar in line:
            if currChar not in dict:
                dict[currChar] = 1
            else:
                dict[currChar] += 1

    maxLength = 0
    countList = []
    for currChar in dict: #turns the dict values into list
        countList.append(dict[currChar])

        currLength = len(str(dict[currChar]))
        if currLength > maxLength: #find maxLength
            maxLength = currLength
    countList.sort()

    for count in countList: #prints the function w/ indent
        for currChar in dict:
            indent = maxLength - len(str(count))
            if count == dict[currChar]:
                print(currChar + " : " + " " * indent + str(count))

docWords = open('words.txt')

wordCount(docWords)
