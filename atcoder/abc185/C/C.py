#!/usr/bin/env pypy3

from functools import lru_cache

@lru_cache(None)
def ans(L, cuts):
    if cuts == 0: return 1
    if L == 0: return 0

    ret = 0
    for i in range(1, L):
        ret += ans(L-i, cuts-1)
    return ret

N = int(input())

print(ans(N, 11))