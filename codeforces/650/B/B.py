#!/usr/bin/env python3
	
def ans(A):
	for i in range(len(A)):
		A[i] = A[i] % 2

	num_zeros = len([a for a in A if a == 0])
	num_ones = len([a for a in A if a == 1])

	if len(A) % 2 == 0:
		if not (num_ones == num_zeros):
			return -1
		else:
			mismatches = 0
			for i, a in enumerate(A):
				if i % 2 != a:
					mismatches += 1
			return mismatches // 2
	else:
		if not (num_ones == num_zeros - 1):
			return -1
		else:
			mismatches = 0
			for i, a in enumerate(A):
				if i % 2 != a:
					mismatches += 1
			return mismatches // 2
T = int(input())
for t in range(T):
	input()
	A = input().split(' ')
	A = [int(x) for x in A]
	print(ans(A))