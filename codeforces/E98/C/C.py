#!/usr/bin/env pypy3

def ans(S):
	num_round = 0
	num_square = 0

	ret = 0

	for c in S:
		if c == '[':
			num_square += 1
		elif c == '(':
			num_round += 1
		elif c == ']':
			if num_square > 0:
				ret += 1
				num_square -= 1
		elif c == ')':
			if num_round > 0:
				ret += 1
				num_round -= 1
		else:
			assert(False)

	return ret

	return S

T = int(input())
for _ in range(T):
	print(ans(input()))
