#!/usr/bin/env pypy3

MODULUS = 10**9+7


def make_nCr_mod(max_n=10**6+50, mod=10**9 + 7):
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        if n < r: return 0
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

nCr_mod = make_nCr_mod()

B, N = input().split(' ')
B = int(B)
K = input().split(' ')
K = [int(x) for x in K if len(x)]

from functools import lru_cache

@lru_cache(maxsize=None)
def dp(b, i):
    if i == len(K):
        if b == 0:
            return 1
        else:
            return 0
    ret = 0
    for first in range(min(b, K[i])+1):
        ret = (ret + dp(b-first, i+1))

    return ret

def slow_ans(B, K):
    return dp(B, 0)

N = B
S = K

import array
psums = array.array('i', [0]*(N+len(S)))
for i in range(N+len(S)):
    psums[i] = (psums[i-1] + nCr_mod(i, len(S)-2))

def fast_ans(N, S):
    ret = nCr_mod(N+len(S)-1, N)
    print("starting", ret)
    for s in S:
        print("subtracting", psums[N+len(S)-3-s])
        ret -= psums[N+len(S)-3-s]
    return ret

print(fast_ans(B,K))
