#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import deque

### CODE HERE

def make_fill(N, M, val):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

def ans(grid):
    R = len(grid)
    C = len(grid[0])
    point = None

    worklist = deque([])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'L':
                point = i, j

    visited = make_fill(R, C, False)

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = point[0]+dx, point[1]+dy
        if not (0 <= new_x < R): continue
        if not (0 <= new_y < C): continue
        if grid[new_x][new_y] == '.': worklist.append((new_x, new_y))

    def good(x, y):
        need_to_block = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x+dx, y+dy
            if not (0 <= new_x < R): continue
            if not (0 <= new_y < C): continue
            if grid[new_x][new_y] == '.': need_to_block += 1
        return need_to_block <= 1

    while len(worklist):
        x, y = worklist.pop()
        if visited[x][y]: continue
        visited[x][y] = True

        if good(x, y):
            grid[x][y] = '+'

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x+dx, y+dy
                if not (0 <= new_x < R): continue
                if not (0 <= new_y < C): continue
                if grid[new_x][new_y] == '.':
                    visited[new_x][new_y] = False
                    worklist.append((new_x, new_y))

    ret = ""
    grid = [''.join(row) for row in grid]
    print('\n'.join(grid))

for _ in range(read_int()):
    N, M = read_int_tuple()
    grid = []
    for _ in range(N):
        grid += [list(input())]
    ans(grid)