#!/usr/bin/env python3

from collections import defaultdict

def ans(A):
	N = len(A)
	M = len(A[0])

	num_0 = defaultdict(int)
	num_1 = defaultdict(int)

	for i in range(N):
		for j in range(M):
			if A[i][j] == 0:
				num_0[i + j] += 1
			else:
				num_1[i + j] += 1

	size = N + M - 1

	ret = 0

	for i in range(size // 2):
		total_num_0 = num_0[i] + num_0[size - i - 1]
		total_num_1 = num_1[i] + num_1[size - i - 1]

		# print("considering levels", i, size-i-1, total_num_0, total_num_1)

		ret += min(total_num_0, total_num_1)

	return ret

T = int(input())
for t in range(T):
	n, m = input().split(' ')
	n = int(n)
	m = int(m)

	rows = []
	for _ in range(n):
		row = input().split(' ')
		row = [int(x) for x in row]
		rows += [row]

	print(ans(rows))