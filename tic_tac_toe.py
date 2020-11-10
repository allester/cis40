"""
Lab 10 - tic_tac_toe.py - De Anza  CIS D040 - Allester Ramayrat
"""

#0123456789
" 1 | 2 | 3  # row 1"
" --|---|--  # filler"
" 4 | 5 | 6  # row 2"
" --|---|--  # filler"
" 7 | 8 | 9  # row 3"
# list length is 10

row1 = list(" 1 | 2 | 3")
row2 = list(" 4 | 5 | 6")
row3 = list(" 7 | 8 | 9")
filler = list(" --|---|--")

def printBoard():
    print("".join(row1))
    print("".join(filler))
    print("".join(row2))
    print("".join(filler))
    print("".join(row3))

def playerInput(playerMove, playerShape): # replaces the player's input # w/ their shape
    for i in range(10):
        if playerMove == row1[i]:
            row1[i] = playerShape
        elif playerMove == row2[i]:
            row2[i] = playerShape
        elif playerMove == row3[i]:
            row3[i] = playerShape

def checkClear(playerMove): # checks if spot is taken
    if playerMove == "1":
        if row1[1] == "x" or row1[1] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "2":
        if row1[5] == "x" or row1[5] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "3":
        if row1[9] == "x" or row1[9] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "4":
        if row2[1] == "x" or row2[1] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "5":
        if row2[5] == "x" or row2[5] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "6":
        if row2[9] == "x" or row2[9] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "7":
        if row3[1] == "x" or row3[1] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "8":
        if row3[5] == "x" or row3[5] == "o":
            clear = False
        else:
            clear = True
    elif playerMove == "9":
        if row3[9] == "x" or row3[9] == "o":
            clear = False
        else:
            clear = True
    return clear

def checkWin(playerShape): # returns True if there is a winner

    # horizontal
    if row1[1] == playerShape and row1[5] == playerShape and row1[9] == playerShape:
        return True
    elif row2[1] == playerShape and row2[5] == playerShape and row2[9] == playerShape:
        return True
    elif row3[1] == playerShape and row3[5] == playerShape and row3[9] == playerShape:
        return True

    # vertical
    elif row1[1] == playerShape and row2[1] == playerShape and row3[1] == playerShape:
        return True
    elif row1[5] == playerShape and row2[5] == playerShape and row3[5] == playerShape:
        return True
    elif row1[9] == playerShape and row2[9] == playerShape and row3[9] == playerShape:
        return True


    # diagonal
    elif row1[1] == playerShape and row2[5] == playerShape and row3[9] == playerShape:
        return True
    elif row1[9] == playerShape and row2[5] == playerShape and row3[1] == playerShape:
        return True

    else:
        return False

def checkTie(): # returns True if there is a tie
    if ((row1[1] == "x" or row1[1] == "o") and (row1[5] == "x" or row1[5] == "o") and (row1[9] == "x" or row1[9] == "o") and
        (row2[1] == "x" or row2[1] == "o") and (row2[5] == "x" or row2[5] == "o") and (row2[9] == "x" or row2[9] == "o") and
        (row3[1] == "x" or row3[1] == "o") and (row3[5] == "x" or row3[5] == "o") and (row3[9] == "x" or row3[9] == "o")):
        return True
    else:
        return False

#def compAlgo():

"""
Main
"""
print("Welcome to Tic-Tac-Toe")
printBoard()
turn = "x"
while True:
    if turn == "x":
        playerMove = input("Player 1 input position to place \"x\": ") # gets input

        if playerMove not in str([1,2,3,4,5,6,7,8,9]): # if input is not a number
            print("Invalid Input.")
            continue

        if checkClear(playerMove): # if place not taken it places x at the number
            playerInput(playerMove, "x")
            turn = "o"
            printBoard()
        else:
            print("You can't place there! Try again!") # reruns turn "x" since variable turn doesn't get reassigned
            continue

        if checkWin("x"): # ends if there is a valid win
            print("Congrats! Player 1 has won!")
            break

        if checkTie(): # ends if there is a tie
            print("It's a tie!")
            break

    else:
        playerMove = input("Player 2 input position to place \"o\": ")

        if playerMove not in str([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            print("Invalid Input.")
            continue

        if checkClear(playerMove):
            playerInput(playerMove, "o")
            turn = "x"
            printBoard()
        else:
            print("You can't place there! Try again!")
            continue

        if checkWin("o"):
            print("Congrats! Player 2 has won!")
            break

        if checkTie():
            print("It's a tie!")
            break