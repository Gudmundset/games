#!/usr/bin/env python 

from random import randint
import sys

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row+1
#print ship_col+1

turn = 0

while turn < 25:
    print "Turn", turn + 1, " /// Pick numbers between 1 and 5. Press q to quit"
    while True:
        try:
            guess_row = raw_input("Guess Row: ")
            guess_col = raw_input("Guess Col: ")
            if str(guess_row).lower() == 'q' or str(guess_col).lower() == 'q':
                print "Ok thanks bye"
                sys.exit(0)
            else:
                guess_row = int(guess_row)
                guess_col = int(guess_col)
            break
        except ValueError:
            print "I didn't catch that. Type again?"
    guess_row = int(guess_row) - 1
    guess_col = int(guess_col) - 1
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Not in ocean. You sunk my land cruiser!"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            turn -= 1
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)
        turn += 1
    if turn == 24:
        print "Game Over."
        break
