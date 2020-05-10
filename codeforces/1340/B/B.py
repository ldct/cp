#!/usr/bin/env pypy3

import sys

sys.setrecursionlimit(2500)

DIGITS = [
	"1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"
]
DIGITS = list(int(d, 2) for d in DIGITS)

def subset(a, b):
	for i in range(7):
		mask = 1 << i
		if a & mask and not b & mask:
			return False
	return True

N, K = input().split(' ')
N, K = int(N), int(K)

arr = []

for n in range(N):
	arr += [int(input(),2)]

num_cache_misses = 0


memo = dict()

def possible(start, budget):
	if budget < 0:
		return False
	if start == N:
		return budget == 0

	if (start, budget) in memo:
		return memo[(start, budget)]
		
	for digit in DIGITS:
		if subset(arr[start], digit):
			cost = bin(arr[start] - digit).count('1')
			if possible(start+1, budget - cost):
				memo[(start, budget)] = True
				return True

	memo[(start, budget)] = False
	return False

if not possible(0, K):
	print("-1")
else:
	budget = K
	for i in range(N):
		for val, digit in list(enumerate(DIGITS))[::-1]:
			cost = bin(arr[i] - digit).count('1')
			if subset(arr[i], digit) and possible(i+1, budget - cost):
				print(val, end='')
				budget -= cost
				break
	print()
