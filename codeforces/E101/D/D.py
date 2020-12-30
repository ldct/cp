#!/usr/bin/env pypy3

import math

def ans(N):

	arr = list(range(1,N+1))

	ret = []
	if N <= 64:
		for i in range(3, N):
			ret += [(i, N)]
			arr[i-1] = math.ceil(arr[i-1] / N)
		while arr[-1] != 1:
			ret += [(N, 2)]
			arr[-1] = math.ceil(arr[-1] / 2)

	else:
		REDUCER = 13

		for i in range(3, N):
			if i == REDUCER: continue

			ret += [(i, N)]
			arr[i-1] = math.ceil(arr[i-1] / N)

		while arr[-1] != 1:
			# print("reducing max")
			ret += [(N, REDUCER)]
			arr[-1] = math.ceil(arr[-1] / REDUCER)

		while arr[REDUCER-1] != 1:
			# print(f"reducing {REDUCER}")
			ret += [(REDUCER, 2)]
			arr[REDUCER-1] = math.ceil(arr[REDUCER-1] / 2)

	assert(len(ret) <= N+5)
	assert(arr.count(1) == N-1)
	assert(arr.count(2) == 1)

	print(len(ret))
	for r in ret:
		print(*r)

for _ in range(int(input())):
	N = int(input())
	ans(N)
