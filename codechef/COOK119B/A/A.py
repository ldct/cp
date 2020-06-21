#!/usr/bin/env pypy3

def ans(B, X):
    ret = 0
    curr_block = None
    for x in X:
        next_block = x // B
        if next_block != curr_block:
            ret += 1
            curr_block = next_block
    return ret

T = int(input())

for _ in range(T):
    N, B, M = input().split(' ')
    B = int(B)
    X = input().split(' ')
    X = list(map(int, X))
    print(ans(B, X))