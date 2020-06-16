#!/usr/bin/env python3
	
import math

def ans(S, K):
	if '1' not in S:
		return math.ceil(len(S) / (K+1))

	runs = S.split('1')
	lr = runs[0]
	rr = runs[-1]
	runs = runs[1:-1]
	runs = [r for r in runs if len(r)]

	ret = 0

	lr = math.ceil((len(lr) - K) / (K+1))
	rr = math.ceil((len(rr) - K) / (K+1))

	runs = [math.ceil((max(0, len(r) - 2*K)) / (K+1)) for r in runs]

	return lr + rr + sum(runs)

T = int(input())
for t in range(T):
	n, K = input().split(' ')
	K = int(K)
	S = input()

	print(ans(S, K))