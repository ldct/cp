#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def odd(M):
    ret = []
    for i in range(M):
        if i % 2 == 0:
            ret += ['+']
        else:
            ret += ['-']
    return ret

def even(M):
    ret = []
    for i in range(M):
        if i % 2 == 0:
            ret += ['|']
        else:
            ret += ['.']
    return ret

def ans(a, b):
    N = 2*a + 1
    M = 2*b + 1
    grid = []
    for i in range(N):
        if i % 2 == 0:
            grid += [odd(M)]
        else:
            grid += [even(M)]

    grid[0][0] = '.'
    grid[0][1] = '.'
    grid[1][0] = '.'

    for row in grid:
        print(''.join(row))

T = int(input())
for t in range(T):
    print("Case #" + str(t+1) + ":")
    ans(*read_int_tuple())
