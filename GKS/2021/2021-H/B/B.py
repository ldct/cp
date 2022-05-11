#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def cost(arr):
    ret = 0
    last_a = None
    for a in arr:
        if a != last_a and a == 1:
            ret += 1
        last_a = a
    return ret

def ans(S):
    N = len(S)
    Y = [0]*N
    R = [0]*N
    B = [0]*N

    for i, s in enumerate(S):
        if s in "YOGA": Y[i] = 1
        if s in "ROPA": R[i] = 1
        if s in "BPGA": B[i] = 1

    return cost(Y) + cost(R) + cost(B)

T = int(input())
for t in range(T):
    input()
    print("Case #" + str(t+1) + ": " + str(ans(input())))
