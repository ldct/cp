#!/usr/bin/env python3

from collections import Counter

def ans(S):
	freqs = Counter(S)
	arg_max = max(freqs, key=freqs.get)
	d = {
		'R': 'P',
		'P': 'S',
		'S': 'R'
	}
	return d[arg_max]*len(S)

T = int(input())
for t in range(T):
	S = input()
	print(ans(S))
