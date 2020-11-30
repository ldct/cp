#!/usr/bin/env python3

from functools import lru_cache

N, K = input().split()
N = int(N)
K = int(K)
S = input()

def winner(x, y):
	if x == y: return x
	if x + y == 'RS': return 'R'
	if x + y == 'PR': return 'P'
	if x + y == 'SP': return 'S'
	return winner(y, x)

@lru_cache(None)
def ans(S, k, i):
	if k == 0:
		return S[i]
	w1 = ans(S, k-1, i)
	w2 = ans(S, k-1, (i + 2**(k-1)) % len(S))

	return winner(w1, w2)

print(ans(S, K, 0))