#!/usr/bin/env pypy3

def ans(A):
	num_ones = 0
	num_twos = 0

	for a in A:
		if a == 1:
			num_ones += 1
		elif a == 2:
			num_twos += 1
		else:
			assert(False)

	if num_twos % 2 == 0 and num_ones % 2 == 0:
		return "YES"

	if num_twos % 2 == 0 and num_ones % 2 == 1:
		return "NO"

	if num_twos % 2 == 1 and num_ones % 2 == 0:
		if num_ones >= 2:
			return "YES"
		return "NO"

	if num_twos % 2 == 1 and num_ones % 2 == 1:
		return "NO"

	return "?"

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	print(ans(A))