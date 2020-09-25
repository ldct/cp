#!/usr/bin/env pypy3

from collections import defaultdict

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

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

MODULUS = 998244353

N, K = input().split()
N = int(N)
K = int(K)

num_start = defaultdict(int)
num_end = defaultdict(int)
indexes = []

for _ in range(N):
	l, r = input().split()
	l = int(l)
	r = int(r)

	num_start[l] += 1
	num_end[r] += 1
	indexes += [l, r]

indexes = sorted(set(indexes))

rs = 0
last_rs = None

ret = 0

for i in indexes:
	rs += num_start[i]

	c = (rs - num_end[i])

	ret += nCr_mod(rs, K)
	ret -= nCr_mod(c, K)

	rs -= num_end[i]

	last_rs = rs

ret %= MODULUS
ret += MODULUS
ret %= MODULUS
print(ret)