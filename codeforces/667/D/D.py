#!/usr/bin/env pypy3

def ans(n, s):
	n = str(n)

	if sum(map(int, n)) <= s:
		return 0

	candidates = set()
	for i in range(1,len(n)):
		na, nb = n[:i], n[i:]
		na = str(int(na)+1)
		nb = "0"*len(nb)
		if sum(map(int, na)) + sum(map(int, nb)) <= s:
			candidates.add(int(na+nb) - int(n))

	big = "1" + "0"*len(n)
	candidates.add(int(big) - int(n))

	small = "1" + "0"*(len(n)-1)
	if int(small) - int(n) >= 0:
		candidates.add(int(small) - int(n))

	return min(candidates)

def ans_slow(n, s):
	for i in range(0, 10**200):
		big = n+i
		big = str(big)
		if sum(map(int, big)) <= s:
			return i

import sys

# print(ans(2,2))
# print(ans_slow(2,2))

# sys.exit(0)

# for s in range(1, 162):
# 	for n in range(1, 10000):
# 		if ans(n,s) != ans_slow(n, s):
# 			print(n, s)

# sys.exit(0)

T = int(input())
for t in range(T):
	n,s = input().split()
	n = int(n)
	s = int(s)

	print(ans(n, s))