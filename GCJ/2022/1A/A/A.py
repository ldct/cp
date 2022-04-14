#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def dup(S, i):
    S = S[:]
    S.insert(i, S[i])
    return S

def ans(S):
    S = list(S)
    i = 0
    while True:
        if i == len(S): break
        if dup(S, i) < S:
            S = dup(S, i)
            i += 1
        i += 1
    return ''.join(S)

T = int(input())
for t in range(T):
    print("Case #" + str(t+1) + ": " + str(ans(input())))
