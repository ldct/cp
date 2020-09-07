#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(N, K, A):
	template = list(A[0:K])

	for _ in range(2):
		num_0 = 0
		num_1 = 0
		num_q = 0

		for c in template:
			if c == '0': num_0 += 1
			elif c == '1': num_1 += 1
			elif c == '?': num_q += 1
			else: assert(False)

		gap = max(num_0, num_1) - min(num_0, num_1)
		if gap > num_q:
			return 'NO'

		for i in range(N):
			a = template[i % K]
			b = A[i]

			if a != '?' and b != '?' and a != b: 
				return 'NO'
			if a == '?' and b != '?':
				template[i % K] = b

	return 'YES'

T = int(input())
for t in range(T):
	N, K = input().split()
	N = int(N)
	K = int(K)
	A = input()
	print(ans(N, K, A))
