# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 06 : Sudoku Draft
# 3. Assignment Description:
#      This program is meant to allow the user to interact with a Sudoku board, making moves regardless of if they are correct or not. This may not be a fully working version of Sudoku, but it does let you save a file and interact with a file.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me, was remembering the logic I've user previously to make the board, such as the logic that scans the box for whether a number is present or not in the rows and columns there. That being said, I finally figured out a solution that makes sense when trying to account for the 9 spaces, filled or not, that make up each box. Beyond that, the rest of the left over difficulty was present in which case do I account for first, when verifying if a number is legal to be put in a spot or not.
# 5. How long did it take for you to complete the assignment?
#      I accidentally already did it by last week's assignment. It took the same time, being 2 hrs and 15 mins back then.

import json
import re

def startGame():
    board = getFile()
    while True:
        displayBoard(board)
        move = getUserMove()
        if move.lower() == 'q':
            saveFile(board)
            quitGame()
            break

        # Check if it even looks like a coordinate
        if not re.fullmatch(r"([A-Ia-i][1-9])|([1-9][A-Ia-i])", move.strip()):
            print(f"ERROR: The value {move.strip()} is invalid input")
            continue

        # Now check if the coordinate is within bounds (0–8)
        if not validCoordinate(move):
            print(f"ERROR: Square {move.strip().upper()} is invalid")
            continue

        col, row = convertCoordinate(move)
        if not (0 <= row < 9 and 0 <= col < 9):
            print(f"ERROR: Square {move.strip().upper()} is invalid")
            continue

        if isFilled(board, row, col):
            print(f"ERROR: Square {move.strip().upper()} is filled")
            continue

        try:
            num = int(input(f"\n> "))
        except ValueError:
            print("ERROR: The value is invalid")
            continue

        if not (1 <= num <= 9):
            print(f"ERROR: The value {num} is invalid")
            continue

        if not isValidRow(board, row, num):
            print(f"ERROR: The value {num} already exists in the row")
            continue

        if not isValidColumn(board, col, num):
            print(f"ERROR: The value {num} already exists in the column")
            continue

        if not isValidBox(board, row, col, num):
            print(f"ERROR: The value {num} already exists in the box")
            continue

        placeNumber(board, row, col, num)

def getFile():
    filename = input("Where is your board located? ")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            board = data['board']
            # Transpose from column-major to row-major
            return [[board[col][row] for col in range(9)] for row in range(9)]
    except Exception as e:
        print(f"Error reading file: {e}")
        exit()

def saveFile(board):
    filename = input("Enter filename to save the board: ")
    try:
        # Transpose from row-major to column-major
        transposed = [[board[row][col] for row in range(9)] for col in range(9)]
        with open(filename, 'w') as f:
            json.dump({"board": transposed}, f)
            print("Board saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def displayBoard(board):
    print("   A B C D E F G H I")
    for i in range(9):
        row = str(i + 1) + "  "
        for j in range(9):
            val = board[i][j]
            row += str(val) if val != 0 else ' '
            if j % 3 == 2 and j != 8:
                row += '|'
            else:
                row += ' '
        print(row)
        if i % 3 == 2 and i != 8:
            print("   -----+-----+-----")

def getUserMove():
    move = input("\nEnter cell (e.g. A1 or 1A) or Q to quit: ")
    return move

def validCoordinate(move):
    move = move.strip().upper()
    match = re.fullmatch(r"([A-I][1-9])|([1-9][A-I])", move)
    return bool(match)

def convertCoordinate(move):
    move = move.strip().upper()
    if move[0].isalpha():
        col = ord(move[0]) - ord('A')
        row = int(move[1]) - 1
    else:
        col = ord(move[1]) - ord('A')
        row = int(move[0]) - 1
    return (col, row)

def isFilled(board, row, col):
    return board[row][col] != 0

def isValidRow(board, row, num):
    return num not in board[row]

def isValidColumn(board, col, num):
    return num not in [board[row][col] for row in range(9)]

def isValidBox(board, row, col, num):
    boxStartRow = (row // 3) * 3
    boxStartCol = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[boxStartRow + i][boxStartCol + j] == num:
                return False
    return True

def placeNumber(board, row, col, num):
    board[row][col] = num

def quitGame():
    print("Thanks for playing Sudoku!")

# Run the game
if __name__ == "__main__":
    startGame()