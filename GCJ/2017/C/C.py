#!/usr/bin/env python3

T = int(input())

def ans(N, K):
	stalls = [False]*(N+2)
	LSs = stalls[:]
	RSs = stalls[:]

	for _ in range(K):
		print('kk')
		for i in range(len(stalls)):
			LSs[i] = 0
			j = i - 1
			while (j >= 0) and (j < N+2) and not stalls[j]:
				LSs[i] += 1
				j -= 1

			RSs[i] = 0
			j = i + 1
			while (j >= 0) and (j < N+2) and not stalls[j]:
				RSs[i] += 1
				j += 1

		maxmin = max(min(RSs[i], LSs[i]) for i in range(N+2))
		minmax = min(max(RSs[i], LSs[i]) for i in range(N+2))

		for i in range(len(stalls)):
			if min(RSs[i], LSs[i]) == maxmin and max(RSs[i], LSs[i]) == minmax:
				print('hi')
				stalls[i] = True
				break

	return stalls

for i in range(T):
	N, K = input().split(' ')
	N, K = int(N), int(K)
	print("Case #" + str(i+1) + ": " + str(ans(N, K)))
