#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))


MODULUS = 998244353

def make_nCr_mod(max_n=5 * 10**5 + 100, mod=998244353):
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

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def ans_slow(S):
    ret = set()
    for ss in subsets(S, low=1):
        for p in permutations(ss):
            ret.add(p)
    return len(ret)

def ans(S):
    freq = []
    for c in ALPHABET:
        freq += [S.count(c)]

    @lru_cache(None)
    def dp(c, l):
        if l == 0: return 1
        if c == -1: return 0
        max_num_c = min(l, freq[c])
        ret = 0

        for num_c in range(max_num_c + 1):
            inc = dp(c-1, l-num_c)*nCr_mod(l, num_c)
            ret += inc
            ret %= MODULUS
        return ret

    ret = 0
    for l in range(1, len(S)+1):
        ret += dp(25, l)
        ret %= MODULUS
    return ret

print(ans(input()))
