def palindrome(string):

    for i in range(len(string)):

        print(string[len(string)-1-i], end = "")

string = input("Type in your word:")

palindrome(string)