#!/usr/bin/env python3

ZERO = 0.0
ONE = 1.0

from functools import lru_cache

def avg(n, cases):
	ret = [ZERO]*n
	b = len(cases)

	for case in cases:
		for i in range(n):
			ret[i] += case[i]

	return tuple([r / b for r in ret])

@lru_cache(None)
def H(n):
	if n == 1: return ONE
	return H(n-1) + (1.0 / n)

@lru_cache(None)
def weights(n):
	if n == 2: return (ONE, ONE)

	base = list(weights(n-1))

	for i in range(len(base)):
		base[i] += 1 / (i+1)

	return (H(n-1),) + tuple(base)

for i in range(2, 5000):
	weights(i)

@lru_cache(None)
def weights_slow(n):
	if n == 2: return (ONE, ONE)

	cases = []

	for i in range(n-1):
		base = list(weights_slow(n-1))
		base = base[0:i] + [base[i]] + base[i:]

		base[i] += ONE
		base[i+1] += ONE

		cases += [tuple(base)]

	return avg(n, cases)

def ans(N, cards):
	w = weights(N)

	ret = ZERO
	for i in range(N):
		ret += w[i] * cards[i]

	return ret


T = int(input())
for t in range(T):
	N = int(input())
	cards = list(map(int, input().split()))

	print("Case #" + str(t+1) + ": " + str(ans(N, cards)))
