# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was interesting! I know it definitely could become a whole other world of difficulty if I wasn't given the game ending logic, the base functions, and the rest of the structure here. Being aware of this, I still found that the mental gymnastics I had to do to figure out display_board and is_x_turn were the hardest. For me, I think this was just tough to wrap my brain around but once I understood how Tic-Tac-Toe works, where it has to be X's turn if they have had the same amount of turns due to it going first, it became much easier. Then, I was able to look deeper into how 'return' works for booleans, allowing me to properly figure out the turn order. For the display, that was weird since I had to allocate for the appropriate range for each row. However, with the power of multiplication I was able to make sure I could account for each row being [0:3], [3:6], and [6:9]. With that all being said, this was fun and I got a chance to go research how to tackle reading from JSON files and writing to JSON files too. Woo!
# 5. How long did it take for you to complete the assignment?
#      2 hrs 19 mins

import json
import os

# The characters used in the Tic-Tac-Toe board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board.
blank_board = {
    "board": [
        BLANK, BLANK, BLANK,
        BLANK, BLANK, BLANK,
        BLANK, BLANK, BLANK
    ]
}

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data["board"]
    else:
        return blank_board["board"]

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, 'w') as file:
        json.dump({"board": board}, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    for row in range(3):
        row_str = " " + " | ".join(board[row * 3: row * 3 + 3]) + " "
        print(row_str)
        if row < 2:
            print("---+---+---")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_count = board.count(X)
    o_count = board.count(O)
    return x_count == o_count

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    display_board(board)
    turn = X if is_x_turn(board) else O
    print(f"{turn}>", end=' ')
    move = input().strip()

    if move.lower() == 'q':
        save_board("game.json", board)
        print("Game saved. Exiting...")
        return False

    if not move.isdigit() or int(move) < 1 or int(move) > 9:
        print("Invalid input. Please enter a number 1-9.")
        return True

    move_index = int(move) - 1
    if board[move_index] != BLANK:
        print("That square is already taken.")
        return True

    board[move_index] = turn

    if game_done(board, message=True):
        # Game over, clear saved game
        if os.path.exists("game.json"):
            os.remove("game.json")
        return False

    return True

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# Main game logic
filename = "game.json"
board = read_board(filename)

while play_game(board):
    pass
