#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import combinations, product

### CODE HERE

H,W,A,B = read_int_tuple()

points = []
for i in range(H):
    for j in range(W):
        points += [(i,j)]

def ok(p, a):
    grid = []
    for _ in range(H):
        grid += [[0]*W]
    for (x,y), (dx,dy) in zip(p, a):
        if grid[x][y] != 0: return False
        grid[x][y] = 1
        x += dx
        y += dy

        if not (0 <= x < H): return False
        if not (0 <= y < W): return False

        if grid[x][y] != 0: return False
        grid[x][y] = 1

    return True

ret = 0
for p in combinations(points, A):
    for a in product([(1,0),(0,1)], repeat=A):
        if ok(p, a):
            ret += 1
            # print(p, a)

print(ret)