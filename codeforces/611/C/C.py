#!/usr/bin/env python2

input = raw_input

h, w = input().split(' ')
h, w = int(h), int(w)

grid = []

for i in range(h):
    grid += [input()]

def isHGood(r, c):
    if c == w: return False
    return grid[r-1][c-1] == "." and grid[r-1][c] == "."

def isVGood(r, c):
    if r == h: return False
    return grid[r-1][c-1] == "." and grid[r][c-1] == "."

numHGoodMemo = {}
def numHGood(r, c):
    # number of h-good cells in rectangle [1, 1]..[r, c]

    if (r, c) in numHGoodMemo: return numHGoodMemo[(r, c)]

    ans = 0
    for x in range(1, r+1):
        for y in range(1, c+1):
            if isHGood(x, y):
                ans += 1

    numHGoodMemo[(r, c)] = ans
    return ans

numVGoodMemo = {}
def numVGood(r, c):

    if (r, c) in numVGoodMemo: return numVGoodMemo[(r, c)]

    ans = 0
    for x in range(1, r+1):
        for y in range(1, c+1):
            if isVGood(x, y):
                ans += 1
    numVGoodMemo[(r, c)] = ans
    return ans

q = int(input())

def numHGood4(r1, c1, r2, c2):
    return numHGood(r2, c2) - numHGood(r1-1, c2) - numHGood(r2, c1-1) + numHGood(r1-1, c1-1)

def numVGood4(r1, c1, r2, c2):
    return numVGood(r2, c2) - numVGood(r1-1, c2) - numVGood(r2, c1-1) + numVGood(r1-1, c1-1)

def numDominoes(r1, c1, r2, c2):
    return numHGood4(r1, c1, r2, c2-1) + numVGood4(r1, c1, r2-1, c2)

ans = ""
for _ in range(q):
    r1, c1, r2, c2 = tuple(int(i) for i in input().split(' '))
    print(numDominoes(r1, c1, r2, c2))
