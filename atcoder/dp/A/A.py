#!/usr/bin/env python3

import functools

N = int(input())

H = input().split(' ')
H = [int(x) for x in H]

@functools.lru_cache(maxsize=None)
def cost(i):
    if i == N-1:
        return 0
    ret = float("inf")

    if i + 1 < N:
        ret = min(ret, abs(H[i+1] - H[i]) + cost(i+1))
    if i + 2 < N:
        ret = min(ret, abs(H[i+2] - H[i]) + cost(i+2))
    
    return ret

print(cost(0))