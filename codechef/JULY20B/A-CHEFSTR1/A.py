#!/usr/bin/env python3

def ans(S):
    ret = 0
    for i in range(len(S)-1):
        ret += max(0, abs(S[i] - S[i+1]) - 1)
    return ret

T = int(input())

for _ in range(T):
    input()
    S = input().split(' ')
    S = list(map(int, S))
    print(ans(S))