#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ok(i, S, T):
    S = list(S)
    S[i], S[i+1] = S[i+1], S[i]
    return S == list(T)

def ans(S, T):
    if S == T: return "Yes"
    for i in range(len(S)-1):
        if ok(i, S, T): return "Yes"
    return "No"

S = input()
T = input()
print(ans(S, T))