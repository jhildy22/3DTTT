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
board = np.array([[0,0,0], [0,0,0], [0,0,0]], np.int32)

# prints menu, prompts user to continue: go -> move, exit -> exit_game
def newGame():
    displayMenu()

    print "When ready type <Go> to begin or <exit> to close the game."
    print

    start = raw_input("Ready? ")
    if start == "go" or start == "GO" or start == "Go":
        print
        # start game
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




# confirm user wants to exit: y -> exit game, n -> reset game
def exit_game():
    user_exit = raw_input("Are you sure you want to go? y/n ")
    if user_exit == "y" or user_exit == "Y":
        exit()
    else:
        reset()











def main():


    print type(board)
    print board.shape
    print board.dtype

main()

