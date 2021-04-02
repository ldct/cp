#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

H, W, X, Y = read_int_tuple()
mat = []
for _ in range(H):
    mat += [list(input())]
X -= 1
Y -= 1

mat[X][Y] = '.'
x, y = X, Y
while x < H and mat[x][y] == '.':
    mat[x][y] = '_'
    x += 1

mat[X][Y] = '.'
x, y = X, Y
while x >= 0 and mat[x][y] == '.':
    mat[x][y] = '_'
    x -= 1

mat[X][Y] = '.'
x, y = X, Y
while y < W and mat[x][y] == '.':
    mat[x][y] = '_'
    y += 1

mat[X][Y] = '.'
x, y = X, Y
while y >= 0 and mat[x][y] == '.':
    mat[x][y] = '_'
    y -= 1

print(''.join(''.join(row) for row in mat).count('_'))
