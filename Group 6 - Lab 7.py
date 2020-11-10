# read line
# get line length
# if length not in dict
# adds length and the string to the length

def words(docWords):
    
    dict = {}
    
    for line in docWords:

        currWord = line.strip()

        length = len(currWord)
        
        if length not in dict:
                
            dict[length] = [currWord]
                
        else:

            dict[length].append(currWord)

    for length in sorted(dict):
        
        words = " ".join(dict[length])

        print(length, ":", words)

docWords = open('words.txt')

words(docWords)
