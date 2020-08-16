#!/usr/bin/env python3

from collections import Counter

T = int(input())

def ans(A):
    A = list(map(int,A))

    B = [0]

    for a in A:
        B += [B[-1] + a - 1]

    cB = Counter(B)

    ret = 0
    for k in cB:
        v = cB[k]
        ret += v*(v-1)//2

    return ret


for t in range(T):
    input()
    print(ans(input()))
