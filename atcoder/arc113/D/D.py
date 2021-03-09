#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

MODULUS = 998244353

def make_nCr_mod(max_n=5*10**5, mod=MODULUS):
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

def ans_very_slow(N, M, K):
    ret = set()
    rows = product(range(1, K+1), repeat=M)
    for mat in product(rows, repeat=N):
        A = tuple(map(min, mat))
        mat = zip(*mat)
        B = tuple(map(max, mat))
        ret.add(A + B)
    return len(ret)

def ans_slow(N, M, K):
    if N == 1: return pow(K, M, MODULUS)
    if M == 1: return pow(K, N, MODULUS)

    ret = 0
    for a in product(range(1, K+1), repeat=N):
        for b in product(range(1, K+1), repeat=M):
            if max(a) <= min(b):
                ret += 1
                ret %= MODULUS

    return ret

def ans(N, M, K):
    if N == 1: return pow(K, M, MODULUS)
    if M == 1: return pow(K, N, MODULUS)

    ret = 0
    for T in range(1, K+1):
        a = pow(T, N, MODULUS) - pow(T-1, N, MODULUS)
        b = pow(K - T + 1, M, MODULUS)
        ret += a*b
        ret %= MODULUS
    return ret

if False:
    for N in range(1, 5):
        for M in range(1, 5):
            for K in range(1, 5):
                if ans(N, M, K) != ans_slow(N, M, K):
                    print(N, M, K)
else:
    N, M, K = read_int_tuple()
    print(ans(N, M, K))