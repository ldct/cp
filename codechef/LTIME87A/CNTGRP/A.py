#!/usr/bin/env pypy3

from collections import Counter

MODULUS = 10**9+7

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()


def make_nCr_mod(max_n=5 * 10**6 + 100, mod=10**9 + 7):
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

ncr = make_nCr_mod()

def ans(N, M, A):
    
    # count number of trees

    A += [0]
    cA = Counter(A)

    k = list(cA.keys())

    ret = 1

    rows = []

    for i in range(1, max(k) + 1):
        rows += [cA[i]]
        if cA[i] == 0: return 0
        ret *= pow(cA[i-1], cA[i], MODULUS)
        ret %= MODULUS

    if M == N-1:
        return ret

    excess = M - (N-1)

    choices = 0
    for r in rows:
        choices += r*(r-1) // 2
        choices %= MODULUS

    return (ret*ncr(choices, excess)) % MODULUS


T = int(input())
for t in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)

    A = list(map(int, input().split()))

    print(ans(N, M, A))