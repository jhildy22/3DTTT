__author__ = 'Richthofen'
import numpy as np



# Global var to hold board
board = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], np.int32)
turn = 'X'
turn_key = {'X':1, 'O':4}

# prints menu, prompts user to continue: go -> move, exit -> exit_game
def newGame():
    displayMenu()

    print "When ready type <Go> to begin or <exit> to close the game."
    print

    start = raw_input("Ready? ")
    if start == "go" or start == "GO" or start == "Go":
        reset()
        move("")
    else:
        exit_game()


# Display intro to user and prompt for start game
def displayMenu():
    print "Welcome to 3d Tic Tac Toe!"
    print "This game tests your memory and spatial intelligence by playing the classic game of tic tac toe"
    print "in three dimensions by memory alone."
    print
    print "The board is set up in three levels from top to bottom: red, yellow, green. Each board is configured like"
    print "battleship, numbers across the top and letters on the side. Each player inputs there turn in the following"
    print "format: Color (level) Column (letter) Row (number).  For example the center of the cube is: Yellow B2."



# reset matrix user turn
def reset():
    global board
    global turn
    board = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], np.int32)
    turn = 'X'


# process user move input and send to helper to verify
def move(error):

    level_row_dictionary = {'r':0, 'y':1, 'g':2, 'a':0, 'b':1, 'c':2, 1:0, 2:1, 3:2 }
    print error
    user_move = raw_input("Player " + turn + ":")

    if len(user_move.split()) != 2:
        move("Invalid input!")

    try:
        level = str(user_move.split()[0][0]).lower()
        row = str(user_move.split()[1][0]).lower()
        col = int(user_move.split()[1][1])

        if level in ['r', 'y','g'] and row in ['a','b','c'] and col in [1,2,3]:
            checkMove(level_row_dictionary[level], level_row_dictionary[row], level_row_dictionary[col])

    except:
        move("Invalid Input!")



def checkMove(level, row, col):
    global turn

    if board[level, col, row] == 0:
        board[level, col, row] = turn_key[turn]
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        checkWinner()
    else:
        endGame("forgot")


def checkWinner():
    loop = [0,1,2]
    count = 0

    for lev in loop:
        count = 0

        for row in loop:
            count = 0
            for col in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame()
        for col in loop:
            count = 0
            for row in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame("")


    for col in loop:
        count = 0

        for lev in loop:
            count = 0
            for row in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame()
        for row in loop:
            count = 0
            for lev in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame("")


    for row in loop:
        count = 0

        for lev in loop:
            count = 0
            for col in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame("")
        for col in loop:
            count = 0
            for lev in loop:
                count += board[lev,col,row]
                if count == 3 or count == 12:
                    endGame("")
    move("")




def endGame(error):

    if error == "forgot":
        print "Player " + turn + ", You forgot the board! You loose!"
        playAgain = raw_input("Do you want to play again? y/n ")
        if playAgain.lower() == 'y':
            newGame()
        else:
            exit_game()


    if turn == 'X':
        winner = 'O'
    else:
        winner = 'X'

    print "We have a winner! Congratulations " + winner + " you have won this round."
    playAgain = raw_input("Do you want to play again? y/n ")
    if playAgain.lower() == 'y':
        newGame()
    else:
        exit_game()
        




# confirm user wants to exit: y -> exit game, n -> reset game
def exit_game():
    user_exit = raw_input("Are you sure you want to go? y/n ")
    if user_exit == "y" or user_exit == "Y":
        exit()
    else:
        newGame()



def main():

    newGame()

main()



# hi there how are you
# today