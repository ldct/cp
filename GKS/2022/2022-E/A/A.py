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

T = int(input())
for t in range(T):
    N = int(input())
    print("Case #" + str(t+1) + ": " + str(ans(N)))
