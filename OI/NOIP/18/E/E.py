#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

MODULUS = 10**9+7

from itertools import product

### CODE HERE

def ok(grid):
    def min_from(x0, y0):
        if not (0 <= x0 < R and 0 <= y0 < C): return None

        ret = 1
        for x in range(x0, R):
            for y in range(y0, C):
                ret = min(ret, grid[x][y])
        return ret

    def max_from(x0, y0):
        if not (0 <= x0 < R and 0 <= y0 < C): return None
        ret = 0
        for x in range(x0, R):
            for y in range(y0, C):
                ret = max(ret, grid[x][y])
        return ret


    R = len(grid)
    C = len(grid[0])
    for x in range(R):
        for y in range(C):
            if min_from(x, y) == 0 and max_from(x-1, y+1) == 1:
                print(x, y)
                return False
    return True

def reshape(seq, R, C):
    ret = []
    for x in range(R):
        row = [seq[x*C + y] for y in range(C)]
        ret += [row]
    return ret

def ans(R, C):
    ret = 0
    for seq in product([0,1], repeat=R*C):
        grid = reshape(seq, R, C)
        if ok(grid):
            ret += 1
            ret %= MODULUS
    return ret

if True:
    R, C = 2,2
    for seq in product([0,1], repeat=R*C):
        grid = reshape(seq, R, C)
        print(grid, ok(grid))
else:
    print(ans(*read_int_tuple()))
