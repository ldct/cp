#!/usr/bin/env pypy3

from collections import defaultdict
from sys import stdin, stdout, exit
 
def input():
    return stdin.readline().strip()

n, k = input().split()
n = int(n)
k = int(k)

freq = defaultdict(int)

for _ in range(n):
	a, b = input().split()
	a = int(a)
	b = int(b)

	freq[a] += b

def ans(k, freq):
	if k == 0:
		ret = max(freq.values())
		if ret == 1:
			return 'NO'
		else:
			return ret
	
	ret = float("-inf")

	vals = list(freq.keys())
	for a in vals:
		if freq[k+a] == 0: continue

		f1 = freq[a]
		f2 = freq[k+a]

		f = min(f1, f2)

		assert(f > 0)

		this_score = f*(k+a+a)
		ret = max(ret, this_score)

	if ret == float("-inf"):
		return 'NO'
	
	return ret


	
print(ans(k, freq))
