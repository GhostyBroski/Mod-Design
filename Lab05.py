# 1. Name:
#      Ash Jones
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program is meant to allow the user to interact with a Sudoku board, making moves regardless of if they are correct or not. This may not be a fully working version of Sudoku, but it does let you save a file and interact with a file.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me, despite having made game boards before, was formatting how it displays the board from the information in the given json file. Wrapping my head around it, I have learned that the internet can be my friend when it comes to accurately grabbing the information. However, displaying it really was a game of figuring out how to accurately space things so it can be displayed properly and then be able to be interactive, so the user can make 'moves' and place numbers. Eventually, while working on it, I realized that I could take advantage of the variables col, num, row, and board to make this process more streamlined and less confusing overall.
# 5. How long did it take for you to complete the assignment?
#      2 hrs 15 mins

import json

def startGame():
    board = getFile()
    while True:
        displayBoard(board)
        move = getUserMove()
        if move.lower() == 'q':
            saveFile(board)
            quitGame()
            break
        if not validCoordinate(move):
            print("Invalid coordinate. Use format like A1, B3, etc.")
            continue

        col, row = convertCoordinate(move)
        try:
            num = int(input("Enter number to place (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a digit between 1 and 9.")
            continue

        if 1 <= num <= 9:
            if isValidMove(board, row, col, num):
                placeNumber(board, row, col, num)
            else:
                print("Invalid move.")
        else:
            print("Please enter a number from 1 to 9.")

def getFile():
    filename = input("Enter the filename of your Sudoku board: ")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data['board']
    except Exception as e:
        print(f"Error reading file: {e}")
        exit()

def saveFile(board):
    filename = input("Enter filename to save the board: ")
    try:
        with open(filename, 'w') as f:
            json.dump({"board": board}, f)
            print("Board saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def displayBoard(board):
    print("   A B C D E F G H I")
    for i in range(9):
        row = str(i + 1) + "  "
        for j in range(9):
            val = board[j][i]
            row += str(val) if val != 0 else ' '
            if j % 3 == 2 and j != 8:
                row += '|'
            else:
                row += ' '
        print(row)
        if i % 3 == 2 and i != 8:
            print("   -----+-----+-----")

def getUserMove():
    move = input("\nEnter cell (e.g. A1) or Q to quit: ")
    return move

def validCoordinate(move):
    if len(move) != 2:
        return False
    columnLetter = move[0].upper()
    rowChar = move[1]
    return columnLetter in 'ABCDEFGHI' and rowChar.isdigit() and 1 <= int(rowChar) <= 9

def convertCoordinate(move):
    columnLetter = move[0].upper()
    rowNumber = int(move[1])
    columnIndex = ord(columnLetter) - ord('A')
    rowIndex = rowNumber - 1
    return (columnIndex, rowIndex)

def isValidMove(board, row, col, num):
    if isFilled(board, row, col):
        print("Square is already filled.")
        return False
    if not isValidRow(board, row, num):
        print("Number already exists in the row.")
        return False
    if not isValidColumn(board, col, num):
        print("Number already exists in the column.")
        return False
    if not isValidBox(board, row, col, num):
        print("Number already exists in the box.")
        return False
    return True

def isFilled(board, row, col):
    return board[col][row] != 0

def isValidRow(board, row, num):
    return num not in [board[col][row] for col in range(9)]

def isValidColumn(board, col, num):
    return num not in [board[col][row] for row in range(9)]

def isValidBox(board, row, col, num):
    boxStartRow = (row // 3) * 3
    boxStartCol = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[boxStartCol + j][boxStartRow + i] == num:
                return False
    return True

def placeNumber(board, row, col, num):
    board[col][row] = num

def quitGame():
    print("Thanks for playing Sudoku!")

# Run the game
if __name__ == "__main__":
    startGame()
