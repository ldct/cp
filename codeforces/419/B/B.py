#!/usr/bin/env pypy3

import math

def make_nCr_mod(max_n=2*10**5 + 100, mod=10**9 + 7):
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

MODULUS = 10**9+7

input()
A = input().split(' ')
A = list(map(int, A))

if len(A) == 1:
    print(A[0])
    exit(0)

if len(A) % 2 == 1:
    new_A = []
    next_plus = True
    for i in range(len(A) - 1):
        if next_plus:
            new_A += [A[i] + A[i+1]]
        else:
            new_A += [A[i] - A[i+1]]
        next_plus = not next_plus
    A = new_A

if len(A) % 4 == 2:
    new_A = []
    for i in range(len(A) // 2):
        new_A += [A[2*i] + A[2*i+1]]
    A = new_A
else:
    new_A = []
    for i in range(len(A) // 2):
        new_A += [A[2*i] - A[2*i+1]]
    A = new_A

# binomial sum

N = len(A)-1

ret = 0

for i in range(N+1):
    ret += A[i]*nCr_mod(N, i)
    ret = ret % MODULUS

print(ret)