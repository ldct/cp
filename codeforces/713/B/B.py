#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(mat):
    rows = set()
    cols = set()
    N = len(mat)
    for x in range(N):
        for y in range(N):
            if mat[x][y] == '*':
                rows.add(x)
                cols.add(y)

    if len(rows) == 1:
        x = list(rows)[0]
        if x + 1 < N:
            rows.add(x + 1)
        else:
            rows.add(x - 1)
    if len(cols) == 1:
        x = list(cols)[0]
        if x + 1 < N:
            cols.add(x + 1)
        else:
            cols.add(x - 1)

    for x in rows:
        for y in cols:
            mat[x][y] = '*'

    return '\n'.join(''.join(s) for s in mat)

    return rows, cols

for _ in range(read_int()):
    N = read_int()
    mat = []
    for _ in range(N):
        mat += [list(input())]

    print(ans(mat))