board = [" "," "," "," "," "," "," "," "," "]
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
    if((board[0]==board[3]==board[6] and board[0]!=" ") or 
       (board[1]==board[4]==board[7] and board[1]!=" ") or 
       (board[2]==board[5]==board[8] and board[2]!=" ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False
def winHorizontal(board):
    global winner
    global currentPlayer
    global gameRunning
    if((board[0]==board[1]==board[2] and board[0]!=" ") or 
       (board[3]==board[4]==board[5] and board[3]!=" ") or 
       (board[6]==board[7]==board[8] and board[6]!=" ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False
def winCross(board):
     global winner
     global currentPlayer
     global gameRunning
     if((board[0]==board[4]==board[8] and board[0]!=" ") or 
       (board[2]==board[4]==board[6] and board[2]!=" ")):
        winner = currentPlayer
        print("Game Over!\nThe Winner is " + winner)
        gameRunning = False

# Check for tie
def checkTie(board):
    global gameRunning
    if(" " not in board):
        print("The game is tied!")
        gameRunning = False

# Working
printBoard(board)
while(gameRunning):
    play = int(input("Enter the position: "))
    if(board[play-1]==" " and (play<=9 and play>=1)):
        board[play-1] = currentPlayer
        printBoard(board)
        winVertical(board)
        winHorizontal(board)
        winCross(board)
        if(winner is None):
            checkTie(board)
        playerSwap()
    else:
        print("Invalid play,retry!")
        continue

