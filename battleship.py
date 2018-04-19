'''
Playing the classic game Battle ship.
Try to guess a random location where a battle ship is.
You have 5 chances to find it.

# Task 1: Convert Python 2 code to Python 3 - DONE
# Tast 2: Add a retry option if player picks a position off the board
# Task 3: Display a grid guide 1-5 for rows and columns

'''
import sys
from random import randint

# Function defintions
def print_board(board):
  print("  0 1 2 3 4")
  row_num = 0
  for row in board:
    print(row_num, " ".join(row))
    row_num += 1
  
  
def random_row(board):
  return randint(0, len(board))

def random_col(board):
  return randint(0, len(board[0]))


print("******************************************")
print("*        Welcome to Battle ship          *")
print("*     Try to sink my battle ship by      *")
print("*   guessing the right rows and columns  *")
print("*       You have 5 tries, good luck!     *")
print("******************************************")

board = []

for x in range(5):
  board.append(["O"] * 5)

print_board(board)




ship_row = random_row(board)
ship_col = random_col(board)
print("Battle Ship Row location: %d" % ship_row)
print("Battle Ship Col location: %d" % ship_col)

turn = 1 
while turn < 7:
    if turn == 6:
        print("\n")
        print("**********************************************")
        print("* Game over, you couldn't sink the battleship *")
        print("*    The battleship is shown with B below   *")
        board[ship_row][ship_col] = "B"
        print_board(board)
        sys.exit()

    print("You are at Turn %d" % turn)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sunk my battleship!")
      sys.exit()
    elif(guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
        print("Oops, that's not even in the ocean.")
        # try to replay the turn, i.e. have the while loop in a function,
    elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
    turn = turn + 1
    print_board(board)
