


def updateBoard(letter, pos, board):
    board[pos] = letter
    return board


def spaceIsFree(pos, board):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, le):
    return (board[7] == le and board[8] == le and board[9] == le) or (board[4] == le and board[5] == le and board[6] == le) or \
            (board[1] == le and board[2] == le and board[3] == le) or (board[1] == le and board[4] == le and board[7] == le) or \
            (board[2] == le and board[5] == le and board[8] == le) or (board[3] == le and board[6] == le and board[9] == le) or \
            (board[1] == le and board[5] == le and board[9] == le) or (board[3] == le and board[5] == le and board[7] == le)


def playerMove(board):
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move, board):
                    run = False
                    #updateBoard('X', move)
                    return move
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def pcMove(board):
    possibleMoves = [index for index, letter in enumerate(board) if letter == ' ' and index != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def mainLoop():
    print('Welcome to Tic Tac Toe!')
    board = [' ' for x in range(10)]
    printBoard(board)

    while not (isBoardFull(board)):
        # if pc is the winner
        if (isWinner(board, 'O')):
            print('Sorry, O\'s won this time!')
            break
        else:
            # player makes move
            move = playerMove(board)
            updateBoard('X', move, board)
            printBoard(board)
        #if player is the winner
        if (isWinner(board, 'X')):
            print('X\'s won this time! Good Job!')
            break
        else:
            # pc makes move
            move = pcMove(board)
            if move == 0:
                print('Tie Game!')
            else:
                updateBoard('O', move, board)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)

    if isBoardFull(board):
        print('Tie Game!')


def main():
    while True:
        answer = input('Do you want to play again? (Y/N)')
        if answer.lower() == 'y' or answer.lower == 'yes':
            print('-----------------------------------')
            mainLoop()
        else:
            break

main()