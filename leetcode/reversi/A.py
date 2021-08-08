#!/usr/bin/env pypy3

DIRECTIONS = []
for dx in [-1,0,+1]:
    for dy in [-1,0,+1]:
        if (dx, dy) != (0, 0):
            DIRECTIONS += [(dx, dy)]

def opponent(c):
    if c == 'W': return 'B'
    if c == 'B': return 'W'
    assert(False)

def is_legal(move, player, board):
    hasbracket = lambda direction: find_bracket(move, player, board, direction)
    return board[move[0]][move[1]] == '.' and any(map(hasbracket, DIRECTIONS))

def ok(bracket):
    x, y = bracket
    return (0 <= x < 8) and (0 <= y < 8)

def find_bracket(square, player, board, direction):
    bracket = (square[0] + direction[0], square[1] + direction[1])

    if not ok(bracket): return False
    if board[bracket[0]][bracket[1]] == player:
        return False
    opp = opponent(player)
    while ok(bracket) and board[bracket[0]][bracket[1]] == opp:
        bracket = (bracket[0] + direction[0], bracket[1] + direction[1])
    if not ok(bracket): return False
    if board[bracket[0]][bracket[1]] == '.': return False
    return True


def checkMove(board, rMove, cMove, color):
    # print(find_bracket((rMove, cMove), color, board, (0, +1)))
    return is_legal((rMove, cMove), color, board)

board = [["W","B","B","W","W","B",".","B"],["W",".",".","W","B",".",".","B"],[".","B","B","B","W",".","W","."],["B","W","B",".","B","W",".","."],["W","W",".","W","B","B","B","."],[".",".",".",".","W",".","B","."],[".",".","B","W","W","B","B","."],["B","B",".","W","B",".","B","."]]


print(checkMove(board, 3, 7, 'W'))