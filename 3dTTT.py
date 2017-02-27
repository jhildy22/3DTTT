__author__ = 'Richthofen'
import numpy as np

'''
newGame:
	displayMenu
	reset
	move

displayMenu:
	print menu


move:
	checkMove

checkMove:
	checkWinner/move

checkWinner:
	endGame/move

endGame:
	drawBoard
	playAgain

playAgain:
	reset/exit
'''


# Global var to hold board
board = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], np.int32)
turn = 'X'

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
    board = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], np.int32)


# process user move input and send to helper to verify
def move(error):
    print error
    user_move = raw_input("Player " + turn + ":")
    level = user_move.split()[0][0]
    col = user_move.split()[1][1]
    row = user_move.split()[1][0]

    try:
        if int(col) in [1,2,3] and str(row).lower in ['a','b','c'] and str(level).lower() in ['r', 'y','g']:
            checkMove(str(level), str(col), int(row))
    except:
        move("Invalid input: Please try again")



def checkMove(level, col, row):
    if board[level, col, row] == 0:
        board[level, col, row] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        checkWinner()
    else:
        endGame(turn)


def checkWinner():
    print "hi there"


def endGame(turn):
    if turn == 'X':
        winner = 'O'
    else:
        winner = 'X'

    print "We have a winner! Congratulations " + winner + "you have won this round."
    playAgain = raw_input("Do you want to play again? y/n")
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
        reset()



def main():

    newGame()

main()



# hi there how are you