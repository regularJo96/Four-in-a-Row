import random
import time

LAST_CHOICE = 0

def main():
    # if the player wants to play the game
    # a True value should be returned by mainMenu()
    # and if a True value is returned, an enemy type should also
    # be returned as a second element
    values = mainMenu()
    if(True in values):
        enemy=values[1]
        
        game(enemy)

    print("...\n...\nGOODBYE")

def game(enemy):
    print("starting GAME with " + enemy + " PLAYER\n\n")
    board = createBoard()

    printBoard(board)
    #starts with player 1
    player=1
    move=0
    values=[]
    #does the move win the game?
    #loop until board is full
    #start with checking the middle piece [3][4]
    while(checkIfBoardIsFull(board) is False):
        if(enemy=="LOCAL"):
            move=makeMove(player,board)
            
            if(player==1):
                values = checkIfWinner(player, move, board)
                player=2
            else:
                values = checkIfWinner(player, move, board)
                player=1
                
        else:
            
            if(player==1):
                move=makeMove(player,board)
                values = checkIfWinner(player, move, board)
                player=2
            else:
                move=AIMove(player,board)
                values = checkIfWinner(player, move, board)
                player=1
        
        printBoard(board)
        
        if(values[0] is True):
            winner = values[1]
            if(enemy=="LOCAL"):
                print("WINNER: Player " + str(winner))
            else:
                if(winner==2):
                    print("WINNER: AI")
                else:
                    print("WINNER: Player " + str(winner))
            break
        
def makeMove(player,board):
    userInput = int(input("Player "+ str(player) + "'s turn"
                          + "\nChoose a column to drop your piece: "))
    while(notAValidMove(userInput, board)):

        print("THAT is NOT a valid column.")
        
        userInput = int(input("\nChoose a column to drop your piece: "))
    spotPieceLanded = dropPiece(player,board,userInput)
    # whitespace below the prompt to make room for the board
    print("")
    return spotPieceLanded


def AIMove(player,board):
    # generate a random column for AI to drop piece
    move = random.randrange(1,8)

    while(notAValidMove(move, board)):
        move = random.randrange(1,8)
    
    spotPieceLanded = dropPiece(player,board,move)
    simulateThinking()
    displayChosenColumn(move)

    print("") # whitespace below the prompt to make room for the board
    return spotPieceLanded

## drops the piece, and returns the coordinates it settles at
def dropPiece(player,board,userInput):
    row = 1 #starts at 1 because of the * at top
    
    
    # userInput is the user's chosen column
    while(board[row+1][userInput] not in [1,2,'*']):
        row=row+1
    board[row][userInput] = player
    spotPieceLanded = [row,userInput]
    return spotPieceLanded

    
def notAValidMove(userInput, board):
    if userInput < 1 or userInput > 7:
        print("That is not a column silly")
        #return true because it's not a valid move
        return True
        
    return columnFull(userInput, board)

def getOutput():
    ## a little code to make sure the same choice doesnt happen 2 times in a row
    global LAST_CHOICE

    choice = random.randrange(0,5)
    
    while(choice == LAST_CHOICE):
        choice = random.randrange(0,5)
        
    LAST_CHOICE = choice
    
    output1 = "Wait a moment while I think about a move\n"
    output2 = "Wait a minute, I'm thinking about a move\n"
    output3 = "Please stand by, this is harder than it looks\n"
    output4 = "Error, Error, Error. Just Kidding. Thinking is hard\n"
    output5 = "$%*$#@#%^&*   (*)__(*)\n"

    choices = [output1, output2, output3, output4, output5]
    return choices[choice]


def simulateThinking():

    output = getOutput()
    
    for char in range(len(output)):
        print(output[char], end='')
        time.sleep(.01)
    for thought in range(4):
        print(".", end=' ')
        time.sleep(.5)
        
def columnFull(column,board):
    return board[1][column] in [1,2]


def checkIfBoardIsFull(board):
    for col in range(1,len(board[1])-1):
        
        if(board[1][col]=='_'):
            return False
    print("\nBOARD is FULL!\n")
    return True

## if any of the checkWin() functions return true,
## there is a winner
def checkIfWinner(player, place, board):
    ## win slot for diagonal, vertical or horizontal
    win = [False,False,False]
    win[0] = checkDiagonal(player,place,board,0)
    win[1] = checkVertical(player,place,board,0)
    win[2] = checkHorizontal(player,place,board,0)
    
    return [True in win,player] 

def checkDiagonal(player,place,board, count):
    topRightToLeft = checkDiagonalTopRightToLeft(player,place,board,count)
    bottomLeftToRight = checkDiagonalBottomLeftToRight(player,place,board,count)

    topLeftToRight = checkDiagonalTopLeftToRight(player,place,board,count)
    bottomRightToLeft = checkDiagonalBottomRightToLeft(player,place,board,count)

    #minus 1 because both left and right diagonal check the same start piece
    win1 = (topRightToLeft + bottomLeftToRight)-1 
    win2 = (topLeftToRight + bottomRightToLeft)-1
    
    if win1 == 4:
        return True
    if win2 == 4:
        return True
    return False

def checkDiagonalTopLeftToRight(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]

    if(spot!=player):
        return count
    count=count+1
    return checkDiagonalTopLeftToRight(player,[row+1,col+1],board,count)

def checkDiagonalBottomRightToLeft(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]

    if(spot!=player):
        return count
    count=count+1
    return checkDiagonalBottomRightToLeft(player,[row-1,col-1],board,count)

        
def checkDiagonalTopRightToLeft(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]

    if(spot!=player):
        return count
    count=count+1
    return checkDiagonalTopRightToLeft(player,[row+1,col-1],board,count)
    
def displayChosenColumn(column):
    output = "I choose column " + str(column)
    for char in range(len(output)):
        print(output[char], end='')
        time.sleep(.07)
        
def checkDiagonalBottomLeftToRight(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]

    if(spot!=player):
        return count
    count=count+1
    return checkDiagonalBottomLeftToRight(player,[row-1,col+1],board,count)
    

def checkVertical(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]
    
    if(count==4):
        return True
    if(spot=="*"):
        return False
    
    if(spot==player):
        count=count+1
        return checkVertical(player,[row+1,col],board,count)
        


def checkHorizontal(player,place,board,count):
    
    left = checkLeft(player,place,board,count)
    right = checkRight(player,place,board,count)

    return (left+right-1)==4
          
def checkLeft(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]
    
    if(spot!=player):
        return count
    
    count=count+1
    return checkLeft(player, [row,col-1],board,count)

def checkRight(player,place,board,count):
    row=place[0]
    col=place[1]
    spot=board[row][col]
    
    if(spot!=player):
        return count
    
    count=count+1
    return checkRight(player, [row,col+1],board,count)

def printBoard(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end='  ')
        print()
    print("")

        
def chooseEnemy():
    
    print("********CHOOSE OPPONENT********\n")
    print("1---------local player")
    print("0--------------AI")
    userInput=-1
    while(True):
        userInput = int(input())
        if(userInput==1):
            return "LOCAL"
        if(userInput==0):
            #figure out how to tell main()
            return "AI"

        
def createBoard():
    return [['*','*','*','*','*','*','*','*','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','_','_','_','_','_','_','_','*'],
             ['*','*','*','*','*','*','*','*','*'],
             [' ','1','2','3','4','5','6','7',' ']]


def mainMenu():
    # I decided to return a list of values,
    # one that holds a boolean for starting the
    # game, and an optional one that holds the
    # enemy type [AI or LOCAL]
    
    print("********CONNECT FOUR********\n")
    print("1--------PLAY GAME")
    print("0----------QUIT")
    userInput=-1
    while(True):
        userInput = int(input())

        if userInput==1:
            enemy = chooseEnemy()
            print("")
            return [True,enemy]
        if userInput==0:
            return [False]
    

main()
