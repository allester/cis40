def prepend_and_append(string, lChar, lCount, rChar, rCount):

    for i in range(lCount):
        
        print(lChar, end = "")

    print(string, end = "")

    for i in range(rCount):

        print(rChar, end= "")

prepend_and_append("penultimate", ">", 0, "<", 0)




