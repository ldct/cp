#!/usr/bin/env pypy3

from functools import lru_cache

MODULUS = 10**9+7

# number of [1,M]^N without two consecutive M's
@lru_cache(None)
def count(N, M, last_was_M):
    if N == 0: return 1
    if last_was_M: return ((M-1)*count(N-1, M, False)) % MODULUS
    return (count(N-1, M, True) + (M-1)*count(N-1, M, False)) % MODULUS

def ans(N, M):

    for n in range(1, N):
        count(n, M, True)
        count(n, M, False)

    ret = count(N, M, False) - (M-1)**N
    ret %= MODULUS
    ret += MODULUS
    ret %= MODULUS
    return ret

N, M = input().split()
N = int(N)
M = int(M)

print(ans(N, M))