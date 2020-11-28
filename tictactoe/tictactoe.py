"""
Tic Tac Toe Player
"""

import math
from random import randint
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# MY CODE
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0

    for row in board:
        for col in row:
            if col == X:
                xcount +=1
            elif col == O:
                ocount +=1
    if xcount == ocount or ocount>xcount:
        return X
    elif xcount > ocount:
        return O


# MY CODE
def actions(board):
    """
    Returns SET of all possible actions tuple(i(row), j(col)) available on the board.
    """
    options = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                options.add((i,j))
    return options


# MY CODE
def result(board, action): #returns a NEW 2d list
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    res = [[EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) == action:
                if board[i][j] == EMPTY:
                    res[i][j] = turn
                else:
                    raise Exception("The move is invalid")
            else:
                res[i][j] = board[i][j] 
    return res

# MY CODE
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        ocount = 0
        xcount = 0
        for col in row:
            if col == X:
                xcount+=1
            elif col == O:
                ocount +=1
        if xcount == 3:
            return X 
        if ocount == 3:
            return O

    for i in range(3):
        if((board[0][i] is not EMPTY) and (board[0][i] == board[1][i] == board[2][i])):
            if board[0][i] == X:
                return X 
            else:
                return O #MIGHT BE WRONG SYNTAX

    if((board[1][1] is not EMPTY) and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]))):
        if board[1][1] == X:
            return X
        else:
            return O
    return None

# MY CODE
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty = 0
    if winner(board) == None:
        for row in board:
            for col in row:
                if col == EMPTY:
                    empty+=1
        return empty == 0
    else:
        return True

# MY CODE
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

# MY CODE
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if isEmpty(board):
        best_move = (random.randint(0,3),random.randint(0,3))
        return best_move
   
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            if minimum(result(board,action)) > v:
                v = minimum(result(board,action))
                best_move = [v ,action]
            
    else:
        v= math.inf
        for action in actions(board):
            if maximum(result(board,action)) < v:
                v = maximum(result(board,action))
                best_move = [v,action]
    
    return best_move[1]

def maximum(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minimum(result(board,action)))

        # print("max")
        # print(v,action)
    return v

def minimum(board ):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v  = min(v, maximum(result(board,action))) 

        # print("min")
        # print(v,action)
    return v

def isEmpty(board):
    for row in board:
        for col in row:
            if col is not EMPTY:
                return False
    return True