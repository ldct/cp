#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()


def ans_slow(A):
	A = sorted(A)
	neg = [a for a in A if a < 0]
	pos = [a for a in A if a > 0]
	zer = [a for a in A if a == 0]

	A = neg+pos+zer

	ret = float("-inf")

	for i in range(0, len(A)):
		for j in range(i+1, len(A)):
			for k in range(j+1, len(A)):
				for l in range(k+1, len(A)):
					for t in range(l+1, len(A)):
						ret = max(ret, A[i]*A[j]*A[k]*A[l]*A[t])

	return ret

def prod(A):
	ret = 1
	for a in A:
		ret *= a
	return ret
	
def ans(A):
	A = sorted(A)
	neg = [a for a in A if a < 0]
	pos = [a for a in A if a > 0]
	zer = [a for a in A if a == 0]

	if len(pos) == 0 and len(zer) == 0:
		return prod(neg[::-1][0:5])

	if len(zer) >= 5:
		zer = [0]*5

	if len(neg) >= 5:
		neg = neg[:5]
	
	if len(pos) >= 5:
		pos = pos[len(pos)-5:]

	assert(len(zer) <= 5)
	assert(len(pos) <= 5)
	assert(len(neg) <= 5)

	A = neg+pos+zer

	ret = float("-inf")

	for i in range(0, len(A)):
		for j in range(i+1, len(A)):
			for k in range(j+1, len(A)):
				for l in range(k+1, len(A)):
					for t in range(l+1, len(A)):
						ret = max(ret, A[i]*A[j]*A[k]*A[l]*A[t])

	return ret

if False:
	import random
	for _ in range(10000):
		test_case = [random.randint(-3, 3) for _ in range(12)]
		if ans(test_case) != ans_slow(test_case):
			print(test_case)
else:
	T = int(input())
	for t in range(T):
		input()
		A = list(map(int, input().split()))
		print(ans(A))