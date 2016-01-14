#!/usr/bin/env python3
import sys

L, R, K = input().split(' ')
L = int(L)
R = int(R)
K = int(K)

def powersOf(K):
	i = 1
	while True:
		yield i
		i *= K

powers = []

for p in powersOf(K):
	if p < L: continue
	if p > R: break
	powers += [p]

if len(powers) == 0:
	print(-1)
else:
	print(' '.join(map(str, powers)))
