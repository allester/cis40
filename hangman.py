"""
Lab 9 - hangman.py - De Anza  CIS D040 - Allester Ramayrat
"""

# Gets a random word from words.txt
import random
docWords = open("words.txt")
docWords = docWords.readlines()
correctWord = list(docWords[random.randint(1,113809) - 1].strip())
guessWord = ["_"] * len(correctWord)

print("Welcome to Hangman!")
attempts = 10
wrongLetters = []
while attempts > 0:

    if "_" not in guessWord:
        print("Congrats! You guessed it!", "".join(correctWord))
        break

    print("".join(guessWord))
    print("Wrong guesses: ", "".join(wrongLetters))
    currGuess = input("Guess a letter: ")
    print()

    if currGuess in guessWord or currGuess in wrongLetters:
        print("That letter has already been guessed!")

    elif currGuess in correctWord:
        for i in range(len(correctWord)):
            if correctWord[i] == currGuess:
                guessWord[i] = correctWord[i]

    else:
        wrongLetters.append(currGuess)
        attempts -= 1

if attempts == 0:
    print("Better luck next time! The word was", "".join(correctWord))