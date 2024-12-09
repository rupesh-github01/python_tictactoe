import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
gameRunning = True
winner = None
currentPlayer = "X"

# Print board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player swap
def playerSwap():
    global currentPlayer
    if(currentPlayer == "X"):
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Check for win 
def winVertical(board):
    global winner
    global currentPlayer
    global gameRunning
    if((board[0] == board[3] == board[6] and board[0] != " ") or
       (board[1] == board[4] == board[7] and board[1] != " ") or
       (board[2] == board[5] == board[8] and board[2] != " ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False

def winHorizontal(board):
    global winner
    global currentPlayer
    global gameRunning
    if((board[0] == board[1] == board[2] and board[0] != " ") or
       (board[3] == board[4] == board[5] and board[3] != " ") or
       (board[6] == board[7] == board[8] and board[6] != " ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False

def winCross(board):
    global winner
    global currentPlayer
    global gameRunning
    if((board[0] == board[4] == board[8] and board[0] != " ") or
       (board[2] == board[4] == board[6] and board[2] != " ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False

# Check for tie
def checkTie(board):
    global gameRunning
    if(" " not in board):
        print("The game is tied!")
        printBoard(board)
        gameRunning = False

def machineMove(board):
    empty_positions = [i for i, space in enumerate(board) if space == " "]
    if empty_positions:
        move = random.choice(empty_positions)
        return move
    return None

# Main Game
print("You play as?")
user = input("Enter X or O: ")

if(user == "X"):
    currentPlayer = "X"
    printBoard(board)
    while(gameRunning):
        # Human player's turn
        if(currentPlayer == "X"):
            play = int(input("Enter the position (1-9): "))
            if(board[play-1] == " " and (play <= 9 and play >= 1)):
                board[play-1] = currentPlayer
                winVertical(board)
                winHorizontal(board)
                winCross(board)
                if(winner is None):
                    checkTie(board)
                if(winner is not None):
                    printBoard(board)
                if gameRunning:
                    playerSwap()
            else:
                print("Invalid play, retry!")
                continue
        # Machine's turn
        else:
            play = machineMove(board)
            if(play is not None):
                board[play] = currentPlayer
                printBoard(board)
                winVertical(board)
                winHorizontal(board)
                winCross(board)
                if(winner is None):
                    checkTie(board)
                if(winner is not None):
                    printBoard(board)
                if gameRunning:
                    playerSwap()
else:
    currentPlayer = "O"
    while(gameRunning):
        # Machine's turn
        if(currentPlayer == "O"):
            play = machineMove(board)
            if(play is not None):
                board[play] = currentPlayer
                printBoard(board)
                winVertical(board)
                winHorizontal(board)
                winCross(board)
                if(winner is None):
                    checkTie(board)
                if gameRunning:
                    playerSwap()
        # Human player's turn
        else:
            play = int(input("Enter the position (1-9): "))
            if(board[play-1] == " " and (play <= 9 and play >= 1)):
                board[play-1] = currentPlayer
                winVertical(board)
                winHorizontal(board)
                winCross(board)
                if(winner is not None):
                    printBoard(board)
                if(winner is None):
                    checkTie(board)
                if gameRunning:
                    playerSwap()
            else:
                print("Invalid play, retry!")
                continue
