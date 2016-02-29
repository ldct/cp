#!/usr/bin/env python3

def numLuckiesWithLength(n):
	assert(1 <= n <= 55)
	return 2**n

def numLuckiesWithLengthAtMost(n):
	return sum(numLuckiesWithLength(i) for i in range(1, n+1))

n = int(input())
print(numLuckiesWithLengthAtMost(n))