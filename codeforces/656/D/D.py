#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

def count_diff(c, S):
    c = chr(c + 97)
    ret = 0
    for s in S:
        if c != s:
            ret += 1
    return ret

memo = None

def ans(c, S):
    global memo

    if len(S) == 1:
        if S == chr(c + 97): return 0
        else: return 1
    
    if (c, S) in memo: return memo[(c, S)]

    mid = len(S) // 2
    left = S[0:mid]
    right = S[mid:]

    ret = min(
        count_diff(c, left) + ans(c+1, right),
        ans(c+1, left) + count_diff(c, right)
    )
    memo[(c, S)] = ret
    return ret

for _ in range(T):
    N = int(input())
    S = input()
    memo = dict()
    print(ans(0, S))