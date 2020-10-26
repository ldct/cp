#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def ans(N, M, rows, cols):
    ret = []
    for _ in range(N):
        ret += [[0]*M]

    row_of = dict()
    col_of = dict()

    for row in rows:
        for i in range(len(row)):
            col_of[row[i]] = i


    for col in cols:
        for i in range(len(col)):
            row_of[col[i]] = i

    for i in range(1, N*M+1):
        r = row_of[i]
        c = col_of[i]
        ret[r][c] = i

    for row in ret:
        print(*row)

for _ in range(int(input())):
    [N, M] = list(map(int, input().split()))
    rows = []
    cols = []
    for _ in range(N):
        rows += [list(map(int, input().split()))]
    for _ in range(M):
        cols += [list(map(int, input().split()))]
    ans(N, M, rows, cols)