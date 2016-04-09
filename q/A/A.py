#!/usr/bin/env python3

from collections import deque

N, K = input().split()
N, K = int(N), int(K)

a = list(map(int, input().split()))

print(N, K, a)

def isIncreasing(arr):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i+1]:
			return False
	return True

def isDecreasing(arr):
	for i in range(len(arr) - 1):
		if arr[i] < arr[i+1]:
			return False
	return True


def score(arr):
	numIsIncreasing = 0
	numIsDecreasing = 0
	for i in range(len(arr)+1):
		for j in range(len(arr)+1):
			if i < j:
				print(arr[i:j])
				if isIncreasing(arr[i:j]): numIsIncreasing += 1
				if isDecreasing(arr[i:j]): numIsDecreasing += 1
	return numIsIncreasing - numIsDecreasing


def scoresSlow(N, K, a):
	ret = []
	for i in range(N - K + 1):
		print(a[i:K+i])
		ret += [score(a[i:K+i])]
	return ret


def _ids(arr):
	ids = []
	for i in range(len(arr)-1):
		x, y = arrr[i], arr[i+1]
		if x == y: ids += ['s']
		if x < y: ids += ['i']
		if x > y: ids += ['d']
	return ids

# def rle(arr):
# 	if len(arr) == 0: return []
	
# 	ret = []
# 	num, item = 1, arr[0]

# 	for i in range(1, len(arr)):
# 		if arr[i] != item:
# 			ret += [(num, item)]
# 			num, item = 1, arr[i]
# 		else:
# 			num += 1

# 	ret += [(num, item)]

# 	return ret

def scores(N, K, a):

	# track the window [windowFirst, windowLast]

	windowFirst = 0
	windowLast = 0

	window = deque()

	ids = _ids(a)

	assert(N >= 1)
	assert(len(ids) >= 1)

	if ids[0] === 'i': score = 1
	if ids[0] === 's': score = 0
	if ids[0] === 'd': score = -1

	def pushRight(kind): 
		# update score after window is extended 1 to the right by @kind
		assert len(window) >= 1

		if len(window) === 1:
			(num, item) = deque.pop()

			if item === 'i' and kind === 'i': 
				score += (num + 1)
				deque.append(num + 1, 'i')
			if item === 'i' and kind === 'd': 
				score -= 1
				deque.append(num, 'i')
				deque.append(1, 'd')
			if item === 'i' and kind === 's': 




