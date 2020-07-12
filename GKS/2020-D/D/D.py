#!/usr/bin/env python3

def ans(S, K, difficulties):
	return which(S-1, S-1, K, difficulties)+1

def which(i, j, x, difficulties):
	if x == 1: return i
	
	if i == 0: return which(j+1, i, x-1, difficulties)
	if j == 0: return which(i+1, j, x-1, difficulties)

	if j == len(difficulties): return which(i-1, j, x-1, difficulties)
	if i == len(difficulties): return which(j-1, i, x-1, difficulties)

	i, j = min(i,j), max(i,j)
	if difficulties[i-1] < difficulties[j]: return which(i-1, j, x-1, difficulties)
	return which(j+1, i, x-1, difficulties)
	
T = int(input())
for t in range(T):
	N, Q = input().split()
	N = int(N)
	Q = int(Q)

	if N >= 2:
		difficulties = input().split()
		difficulties = list(map(int, difficulties))
	else:
		difficulties = []

	s = "Case #" + str(t+1) + ": "
	for q in range(Q):
		S, K = input().split()
		S = int(S)
		K = int(K)

		s += str(ans(S, K, difficulties))
		if q < Q-1:
			s += " "

	print(s)
