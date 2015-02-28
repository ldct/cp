#!/usr/bin/env python

import sys
sys.setrecursionlimit(2500)

N, P, T = raw_input().split(' ')
N = int(N)
P = float(P)
T = int(T)

memo = []
for i in range(2001):
	row = []
	for j in range(2001):
		row += [-1]
	memo += [row]

def Z(t, n):
	if t == 0:
		return int(n == 0)
	if memo[t][n] == -1:
		if n == N:
			memo[t][n] = Z(t - 1, n) + Z(t - 1, n - 1) * P
		else:
			memo[t][n] = Z(t - 1, n) * (1 - P) + Z(t - 1, n - 1) * P
	return memo[t][n]

S = 0
for j in range(0, N + 1):
	S += j * Z(T, j)

print(Z(3, 0))