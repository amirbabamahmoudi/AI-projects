import numpy as np
import random
import pygame
import sys
import math
from copy import deepcopy

row_number = 6
column_number = 7

PLAYER = 0
AI = 1

empty = 0
human_piece = 1
ai_piece = 2

#creating an empty arena
def initial_state():
    board = np.zeros((row_number, column_number))
    return board

#dropping a peice in a section of table
def put_piece(board, row, col, piece):
    board[row][col] = piece

#checks if a column has an empty space
def validate_location(board, col):
    return board[row_number - 1][col] == 0
#gives us all columns which still have empty spaces
def valid_columns(board):
    valid_locations = []
    for col in range(column_number):
        if validate_location(board, col):
            valid_locations.append(col)
    return valid_locations
#gives the first row of a column which a playe could put its piece in it
def first_valid_row(board, col):
    for r in range(row_number):
        if board[r][col] == 0:
            return r
#printing the matrix of game table
def print_board(board):
    print(np.flip(board, 0))
#checks if we are in terminal or not
def check_termination(board):
    if check_winner_existence(board, human_piece
            ) or check_winner_existence(
            board, ai_piece) or len(valid_columns(board)) == 0:
        return True
    else:
        return False
#checks if there exists a winner or not
def check_winner_existence(board, piece):
    # Check horizontal locations for win
    for c in range(column_number - 3):
        for r in range(row_number):
            if board[r][c] == piece and board[r][c + 1
            ] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(column_number):
        for r in range(row_number - 3):
            if board[r][c] == piece and board[r + 1][c
            ] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(column_number - 3):
        for r in range(row_number - 3):
            if board[r][c] == piece and board[r + 1][c + 1
            ] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(column_number - 3):
        for r in range(3, row_number):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

#Evaluate function
def eval(window, piece):
    score = 0

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2
    if piece == human_piece and window.count(ai_piece) == 3 and window.count(empty) == 1:
        score -= 4
    if piece == ai_piece and window.count(human_piece) == 3 and  window.count(empty) == 1:
        score -= 4

    return score

#calculating the thotal score of a state for a player
def total_score(board, piece):
    score = 0

    ## Score center column
    center_array = list(board[ : , 3])
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Vertical
    for c in range(column_number):
        for r in range(row_number - 3):
            window = list(board[:, c])[r:r + 4]
            score += eval(window, piece)

    ## Score posiive sloped diagonal
    for r in range(row_number - 3):
        for c in range(column_number - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += eval(window, piece)

    ## Score Horizontal
    for r in range(row_number):
        for c in range(column_number - 3):
            window = list(board[r, :])[c:c + 4]
            score += eval(window, piece)

    for r in range(row_number - 3):
        for c in range(column_number - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            score += eval(window, piece)

    return score

#implementation of alpha-beta algorighm
def alpha_beta_search(board, depth, alpha, beta):
    return max_value(board , depth , alpha , beta )


def max_value(board , depth , alpha , beta ):
    is_terminal = check_termination(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner_existence(board, ai_piece):
                return (None, 10000000000)
            elif check_winner_existence(board, human_piece):
                return (None, -10000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, total_score(board, ai_piece))
    valid_locations = valid_columns(board)
    value = -math.inf
    column = random.choice(valid_locations)
    for col in valid_locations:
        row = first_valid_row(board, col)
        b_copy = deepcopy(board)
        put_piece(b_copy, row, col, ai_piece)
        new_score = min_value(b_copy, depth - 1, alpha, beta)[1]
        if new_score > value:
            value = new_score
            column = col
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return column, value

def min_value(board , depth , alpha , beta ):
    is_terminal = check_termination(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner_existence(board, ai_piece):
                return (None, 10000000000)
            elif check_winner_existence(board, human_piece):
                return (None, -10000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, total_score(board, ai_piece))
    valid_locations = valid_columns(board)
    value = math.inf
    column = random.choice(valid_locations)
    for col in valid_locations:
        row = first_valid_row(board, col)
        b_copy = deepcopy(board)
        put_piece(b_copy, row, col, human_piece)
        new_score = max_value(b_copy, depth - 1, alpha, beta)[1]
        if new_score < value:
            value = new_score
            column = col
        beta = min(beta, value)
        if alpha >= beta:
            break
    return column, value

yellow =  (255, 255, 0)
white =(255, 255, 255)
blue =  (0, 0, 255 )
red = (255 , 0, 0)

#creating the graphical parts of the game
def show_board(board):
    for c in range(column_number):
        for r in range(row_number):
            pygame.draw.rect(screen, yellow, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, white, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(column_number):
        for r in range(row_number):
            if board[r][c] == human_piece:
                pygame.draw.circle(screen, blue, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == ai_piece:
                pygame.draw.circle(screen, red, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = initial_state()
print_board(board)
game_over = False

pygame.init()

SQUARESIZE = 100

width = column_number * SQUARESIZE
height = (row_number + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
show_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

turn = random.randint(PLAYER, AI)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, white, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, blue, (posx, int(SQUARESIZE / 2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, white, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if validate_location(board, col):
                    row = first_valid_row(board, col)
                    put_piece(board, row, col, human_piece)

                    if check_winner_existence(board, human_piece):
                        label = myfont.render("Player 1 wins!!", 1, blue)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    print_board(board)
                    show_board(board)

    # # Ask for Player 2 Input
    if turn == AI and not game_over:

        # col = random.randint(0, column_number-1)
        # col = pick_best_move(board, ai_piece)
        col, alpha_beta_search_score = alpha_beta_search(board, 4, -math.inf, math.inf)

        if validate_location(board, col):
            # pygame.time.wait(500)
            row = first_valid_row(board, col)
            put_piece(board, row, col, ai_piece)

            if check_winner_existence(board, ai_piece):
                label = myfont.render("Player 2 wins!!", 1, red)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            show_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)
