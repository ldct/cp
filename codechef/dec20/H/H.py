#!/usr/bin/env pypy3

from functools import lru_cache

MODULUS = 998244353

if False:
    N = 10
    A = [1]*N
else:
    N = int(input())
    A = list(map(int, input().split()))

@lru_cache(None)
def f(N, B, S):
    if N == 1:
        if B > S: return 1
        return 0

    ret = 0
    for b in range(B):
        new_S = S - A[N-1]*b
        new_S %= 239
        new_S += 239
        new_S %= 239

        ret += f(N-1, b, new_S)
        ret %= MODULUS

    return ret

import math
ret = f(N, 239, 0)
ret *= math.factorial(N)
ret %= MODULUS
print(ret)
