import itertools
import time


def crosswordPuzzle(board, clues, size):
    if len(clues) == 0:
        displayBoard(board)
        return board
    attr = findStart(board, size)
    for clue in clues:
        boardCopy = [row[:] for row in board]
        cluesCopy = clues[:]
        currPos = attr[0]
        if len(clue) == currPos[3]:
            for char in clue:
                if boardCopy[currPos[0]][currPos[1]] not in [char, '-']:
                    return False
                else:
                    boardCopy[currPos[0]][currPos[1]] = char
                    if currPos[2] == 'h':
                        currPos[1] += 1
                    else:
                        currPos[0] += 1
        cluesCopy.remove(clue)
        if crosswordPuzzle(boardCopy, cluesCopy, size):
            return True
    return False

def displayBoard(board):
    print("\n".join([''.join(row) for row in board]))

def getKey(item):
    return item[2]

def findStart(board, size):
    attr = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == '-':
                k = j
                while k > 0 and board[i][k - 1] != '#':
                    k -= 1
                length = findLen(board, [i, k], 'h')
                temp = [i, k, 'h', length]
                if length != 1 and temp not in attr:
                    attr.append([i, k, 'h', length])

                k = i
                while k > 0 and board[k - 1][j] != '#':
                    k -= 1
                length = findLen(board, [k, j], 'v')
                temp = [k, j, 'v', length]
                if length != 1 and temp not in attr:
                    attr.append([k, j, 'v', length])
    return attr

def findLen(board, start, direction):
    length = 1
    currPos = start[:]
    if direction == 'h':
        while currPos[1] < len(board[currPos[0]]) - 1 and board[currPos[0]][currPos[1] + 1] != '#':
            currPos[1] += 1
            length += 1
    else:
        while currPos[0] < len(board) - 1 and board[currPos[0] + 1][currPos[1]] != '#':
            currPos[0] += 1
            length += 1
    return length

if __name__ == "__main__":
    start_time = (time.time() * 200)


    filename = input('File name : ')
    text = open(filename, 'r')
    print(text.read())

   board = []
   boardIdx = 0
   for boardIdx in range(size):
      boardNextLine = str(text.readline().strip())
      board.append(boardNextLine)
   clues = text.readline().strip().split(';')
   board = [list(row) for row in board]
   result = crosswordPuzzle(board, clues, size)
   print(displayBoard(board))

    print("--- %s milliseconds ---" % (((time.time() * 200)) - start_time))
