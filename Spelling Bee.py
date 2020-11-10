def spelling(docWords):

    inputList = list(input("Input characters: "))

    reqChar = input("Input required character: ")

    for currWord in docWords:

        inList = True

        currWord = list(currWord.strip())

        for currChar in currWord:

            if currChar not in inputList:
               
                inList = False

        if inList and (reqChar in currWord) and (len(currWord) > 3):

            print("".join(currWord))
        
docWords = open('words.txt')

spelling(docWords)
