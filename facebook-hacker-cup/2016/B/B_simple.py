#!/usr/bin/env python3

T = int(input())

def numWinning(N, arr, P):
	# number of indices (a, b) such that sum(arr[a:b]) <= P
	# with [a, b) nonempty

	ans = 0

	for a in range(N):
		for b in range(a+1, N+1):
			if sum(arr[a:b]) <= P: 
				ans += 1
	return ans
	 
for t in range(T):

	N, P = input().split()
	N, P = int(N), int(P)
	arr = [int(b) for b in input().split()]

	# if t+1 != 2: continue
	print("Case #" + str(t+1) + ": " + str(numWinning(N, arr, P)))
