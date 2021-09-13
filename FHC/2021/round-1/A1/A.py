#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):
    S = S.replace('F', '')
    ret = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            ret += 1
    return ret

for t in range(read_int()):
    input()
    S = input()
    print(f"Case #{t+1}: {ans(S)}")