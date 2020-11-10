"""
Lab 5 - word_lengths.py - De Anza  CIS D040 - Allester Ramayrat
"""


docWords = open('words.txt')

longNum = 0
longWord = ""
shortNum = 100
shortWord = ""
totalNum = 0
count = 0

for line in docWords:
    currWord = line.strip()
    count += 1
    totalNum += len(currWord)
    avgWord = totalNum / count


    if len(currWord) > longNum:

        longWord = currWord
        longNum = len(currWord)

    if len(currWord) < shortNum:

        shortWord = currWord
        shortNum = len(currWord)



print("The longest words are", longNum, "characters; an example is", longWord)
print("The shortest words are", shortNum, "characters; an example is", shortWord)
print("The average word length is", avgWord)