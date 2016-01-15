#!/usr/bin/env python3

T = int(input())

def numWinning(N, arr, P):

	# number of indices (a, b) such that sum(arr[a:b]) <= P
	# with [a, b) nonempty

	prefixSum = [0] # prefixSum[i] = sum(arr[0:i])

	for i in range(N):
		prefixSum += [prefixSum[i] + arr[i]]

	# for i in range(N-1):
	# 	assert(prefixSum[i] == sum(arr[0:i]))

	def sumArr(a, b):
		# assert(sum(arr[a:b]) == prefixSum[b] - prefixSum[a])
		return prefixSum[b] - prefixSum[a]

	ans = 0

	# print(arr, P)

	for a in range(N):

		# for b in range(a+1, N+1):
		# 	if sumArr(a, b) <= P: 
		# 		ans += 1
		# continue

		# find largest b such that sum(arr[a:b]) <= P

		lo = a+1
		hi = N

		if sumArr(a, lo) > P:
			continue
		elif sumArr(a, hi) <= P:
			# print('hi', a, hi)
			ans += (hi - a)
		else:
			# sumArr(a, lo) <= P
			# sumArr(a, hi) > P

			while hi - lo > 1:
				mid = (lo + hi) // 2
				if sumArr(a, mid) <= P:
					lo = mid
				else:
					hi = mid

			assert(sumArr(a, lo) <= P)
			assert(sumArr(a, lo+1) > P)
			assert(sumArr(a, hi) > P)

			# print('yolo', a, lo)

			ans += (lo - a)

	return ans
	 
for t in range(T):


	N, P = input().split()
	N, P = int(N), int(P)
	arr = [int(b) for b in input().split()]

	print("Case #" + str(t+1) + ": " + str(numWinning(N, arr, P)))
