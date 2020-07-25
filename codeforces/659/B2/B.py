#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(D, K, L):
	zones = []
	for d in D:
		i = L-d
		if 0 > i:
			return -1
		if i >= K:
			zones += [((0, K), (K, 2*K))]
		else:
			zones += [((0, i), (2*K-i, 2*K))] 
	return zones

T = int(input())

for _ in range(T):
	N, K, L = input().split(' ')
	K = int(K)
	L = int(L)
	D = input().split(' ')
	D = list(map(int, D))
	print(ans(D, K, L))