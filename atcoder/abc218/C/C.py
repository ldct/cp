#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def sig(N, S):
    ret = set()
    min_x = float("inf")
    min_y = float("inf")
    for x in range(N):
        for y in range(N):
            if S[x][y] == '#':
                min_x = min(min_x, x)
                min_y = min(min_y, y)
    for x in range(N):
        for y in range(N):
            if S[x][y] == '#':
                ret.add((x-min_x, y-min_y))

    return ret

def rot(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def ans(N, S, T):
    st = sig(N, T)
    for _ in range(10):
        S = rot(S)
        if sig(N, S) == st:
            return "Yes"
    return "No"

N = read_int()
S = []
for _ in range(N):
    S += [input()]
T = []
for _ in range(N):
    T += [input()]
print(ans(N, S, T))