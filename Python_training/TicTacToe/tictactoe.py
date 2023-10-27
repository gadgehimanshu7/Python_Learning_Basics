board = [' ' for x in range(10)]


def insertletter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printboard(board):
    print('    |   |    ')
    print(' ' + board[1] + '  | ' + board[2] + ' |  ' + board[3])
    print('    |   |    ')
    print('-------------')
    print('    |   |    ')
    print(' ' + board[4] + '  | ' + board[5] + ' |  ' + board[6])
    print('    |   |    ')
    print('-------------')
    print('    |   |    ')
    print(' ' + board[7] + '  | ' + board[8] + ' |  ' + board[9])
    print('    |   |    ')


def isBoardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def iswinner(b, l):
    if ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[3] == l and b[6] == l and b[9] == l)):
        return True
    else:
        return False


def playermove():
    run = True
    while run:
        move = input('please select a position to enter X between 1 to 9 : ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertletter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print('Type a valid number between 1 to 9 ')

        except:
            print('Please type a number')


def compmove():
    possiblemoves = [x for x, letter in enumerate(board) if
                     letter == ' ' and x != 0]  # possible moves are just the numerical values.
    move = 0
    for let in ['O', 'X']:  # let as variable for all the possible values as 'O' and 'X'
        for i in possiblemoves:
            boardcopy = board[:]  # boardcopy variable will contain the list.
            boardcopy[
                i] = let  # then boardcopy will get updated at that particular location 'i' i.e. in the possible moves equal to 'let'
            if iswinner(boardcopy, let):
                move = i
                return move

    cornersopen = []
    for i in possiblemoves:
        if i in [1, 3, 7, 9]:
            cornersopen.append(i)

    if len(cornersopen) > 0:
        move = selectrandom(cornersopen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgesopen = []
    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = selectrandom(edgesopen)
        return move

def selectrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("welcome to the game ^-^")
    printboard(board)

    while not(isBoardfull(board)):
        if not(iswinner(board,'O')):     #second parameter as letter for computer.
            playermove()
            printboard(board)

        else:
            print("sorry! you loose.")
            break

        if not(iswinner(board, 'X')):
            move = compmove()
            if move == 0:
                print('')

            elif not (isBoardfull(board)):
                insertletter('O', move)
                print('Computer placed an O on position' , move ,'.')
                printboard(board)
        else:
            print('you win')
            break


    if isBoardfull(board):
        print("tie game")




while True:
    x = input('Shall we begin with the game? (y/n)')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------')
        main()
        x = input('Do u want to play the game again? (y/n)')
    else:
        break


