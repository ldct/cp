#!/usr/bin/env pypy3
	
def alt_sum(A):
	a = 0
	b = 0
	for i in range(len(A)):
		if i % 2 == 0:
			a += A[i]
		else:
			b += A[i]
	return (a, b)

def ans(A):
	n = len(A)
	while True:
		(a, b) = alt_sum(A)

		if a == b:
			assert(len(A) >= n // 2)
			print(len(A))
			print(*A)
			return

		if a > b:
			aa = 0
			bb = 0
			for i in range(len(A)-1, -1, -1):
				if i % 2 == 0:
					aa += A[i]
				else:
					bb += A[i]
				if i % 2 == 0 and A[i] == 1 and aa > bb:
					del A[i]
					break


		elif b > a:
			aa = 0
			bb = 0
			for i in range(len(A)-1, -1, -1):
				if i % 2 == 0:
					aa += A[i]
				else:
					bb += A[i]
				if i % 2 == 1 and A[i] == 1 and bb > aa:
					del A[i]
					break
		else:
			assert(False)

if False:	
	import random, sys
	for _ in range(100000):
		test_case = [random.choice([0, 1]) for _ in range(6)]
		print("tc=", test_case)
		ans(test_case)
	sys.exit(0)

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	ans(A)