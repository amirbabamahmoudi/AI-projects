import copy
import time
import numpy as np

def create_board(n):
    return np.zeros((n, n))

def is_consistent(board, row, col):

    for j in range(col):
        if board[row][j] == 1:
            return False

    a, b = row, col
    while a >= 0 and b >= 0:
        if board[a][b] == 1:
            return False
        a = a - 1
        b = b - 1

    c, d = row, col
    while c < len(board) and d >= 0:
        if board[c][d] == 1:
            return False
        c = c + 1
        d = d - 1

    return True


def back_track(board, col):
    if col >= len(board):
        print(board)
        return True

    for i in range(len(board)):
        if is_consistent(board, i, col):
            board[i][col] = 1
            if back_track(board, col + 1):
                return True
            board[i][col] = 0
    return False

def put_threat(board , row , col , n):
    for c in range(col + 1 , len(board)):
        board[row][c] = n

    a , b = row - 1 , col + 1
    while a >= 0 and b < len(board):
        board[a ][b ] = n
        a = a-1
        b = b+1

    c , d = row + 1 , col + 1
    while c < len(board) and d < len(board):
        board[c ][d ] = n
        c = c+1
        d = d+1

def forward_check(board, col):
    if col >= len(board):
        #print(board)
        return True

    for i in range(len(board)):

        if is_consistent(board, i, col) and board[i][col] != 2:
            put_threat(board , i , col , 2)
            board[i][col] = 1
            if forward_check(board, col + 1):
                return True
            board[i][col] = 0
            put_threat(board, i, col, 0)

    return False


#print(b)
matrix1 = create_board(16)
matrix2 = create_board(16)

#back_track(matrix, 0)
tic1 = time.time()
forward_check(matrix1 , 0)
toc2 = time.time()
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if matrix1[i][j] == 2 :
            matrix1[i][j] = 0
print(matrix1)
print("\n\n")

tic = time.time()
back_track(matrix2 , 0)
toc = time.time()
print("forward_check : ",toc2 - tic1)
print("back track : ",toc - tic)
#print(matrix)

#print(time.time() - tic)


