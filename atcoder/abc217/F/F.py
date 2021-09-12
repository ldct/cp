#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

MODULUS = 998244353

from collections import defaultdict
from functools import lru_cache

def make_nCr_mod(max_n=1000, mod=MODULUS):
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

neighbours = defaultdict(list)

N, M = read_int_tuple()
for _ in range(M):
    a, b = read_int_tuple()
    a -= 1
    b -= 1
    neighbours[a] += [b]

for k in neighbours:
    neighbours[k] = sorted(neighbours[k])

memo = []
for _ in range(2*N+1):
    memo += [[-1]*(2*N+1)]

def ans(i, k):
    if ((k-i) % 2) == 1: return 0
    if i >= k: return 1
    ret = 0
    if i not in neighbours: return 0

    if memo[i][k] != -1: return memo[i][k]

    for j in neighbours[i]:
        if j >= k: break
        inner = ans(i+1, j)
        if inner == 0: continue
        outer = ans(j+1, k)
        if outer == 0: continue

        inner_merges = (j-(i+1)) // 2
        outer_merges = (k-(j+1)) // 2

        inner *= outer
        inner %= MODULUS
        inner *= nCr_mod(inner_merges+outer_merges+1, inner_merges+1)
        inner %= MODULUS

        ret += inner
        ret %= MODULUS

        """
        ------------
        |          |
        v   inner  v outer
        """

    memo[i][k] = ret
    return ret

print(ans(0, 2*N))
