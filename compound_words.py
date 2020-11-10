"""
FINAL EXAM Q 13 - compound_words.py - De Anza  CIS D040 - Allester Ramayrat
"""

compoundWord = input("Enter a word to test whether it's a compound word candidate: ")
docWords = open("words.txt")
list = []
for line in docWords:
    line = line.strip()
    if line in compoundWord:
        list.append(line)
found = False
for word1 in list:
    if found:
        break
    for word2 in list:
        if (word1 + word2 == compoundWord):
            print(compoundWord, " is composed of \'", word1, "\' and \'", word2, "\'.", sep = "")
            found = True
        elif (word2 + word1 == compoundWord):
            print(compoundWord, " is composed of \'", word2, "\' and \'", word1, "\'.", sep = "")
            found = True