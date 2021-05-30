#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

MODULUS = 998244353

def make_nCr_mod(max_n=5 * 10**5 + 100, mod=MODULUS):
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
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

### CODE HERE

@lru_cache(None)
def f(N, K, Q):
    # print(f"f {N} {K} {Q}")
    if Q == 0 and N == 0: return 1
    if Q == 1 and N == K: return 1
    if Q < 0: return 0
    if N < 0: return 0
    ret = (f(N-1, K, Q) + f(N-K-1, K, Q-1)) % MODULUS
    # print(f"f {N} {K} {Q} = {ret}")
    return ret

def count_partitions_interval(n, N, l=0, r=None):
    """
    Number of tuples x_1, x_2 ... x_n such that
    x_i \in [l, r]
    \sum x_i = N
    """

    if r is None: r = N

    N -= n*l
    r -= l

    ret = 0
    UB = min(n, N // (r+1))
    for q in range(0, 1+UB):
        if n < 0: continue
        if N - q*(r+1) + n-1 < 0: continue
        ret += (-1)**q * nCr_mod(n, q) * nCr_mod(N - q*(r+1) + n-1, n-1)

    # print(f"cpi {n} {N} {l} {r} = {ret}")
    return ret

def f_fast(N, K, Q):
    return count_partitions_interval(Q+1, N+2-K*Q, 1, None)

for _ in range(read_int()):
    print(f_fast(*read_int_tuple()) % MODULUS)