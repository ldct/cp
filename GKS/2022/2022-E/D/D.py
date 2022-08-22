#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(N):

    ret = 0
    while N >= 1:
        ret += 1
        N -= 2

        N -= 3

    return ret

def read_dir():
    return input()

T = int(input())
for t in range(T):
    N, P, M, x0, y0 = read_int_list()

    dirs = [read_dir() for _ in range(4)]

    customers = [input() for _ in range(P)]

    print("Case #" + str(t+1) + ": " + str(ans(N)))
