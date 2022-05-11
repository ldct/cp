#!/usr/bin/env python2

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def ans2(N, A, B, C, invisible):
	matrix = [0]*N

	A_start = N-A

	for i in range(A):
		matrix[i] = A_start + i
	
	for i in range(A, A+invisible):
		matrix[i] = 1
	
	for i in range(A+invisible, A+invisible+C):
		matrix[i] = N

	height = N-1
	for i in range(A+invisible+C, A+invisible+C+B):
		matrix[i] = height
		height -= 1

	return matrix

def ans_middle(N, C, invisible):
	matrix = [0]*N

	matrix[0] = N
	C -= 1

	for i in range(1, 1+invisible):
		matrix[i] = 1
	
	for i in range(1+invisible, 1+invisible+C):
		matrix[i] = N

	return matrix

def ans(N, A, B, C):
	A -= C
	B -= C

	if A < 0 or B < 0:
		return 'IMPOSSIBLE'

	if A+B+C > N:
		return 'IMPOSSIBLE'

	invisible = N-(A+B+C)

	if A == 0 and B == 0 and C <= 1:
		if invisible == 0:
			assert(N == 1)
			return '1'
		else:
			return 'IMPOSSIBLE'

	if A == 0 and B == 0:
		assert(C > 1)
		r = ans_middle(N, C, invisible)
		return ' ' .join(map(str, r))

	if A == 0:
		assert(B > 0)
		r = ans2(N, B, A, C, invisible)
		r = reversed(r)
		return ' ' .join(map(str, r))

	r = ans2(N, A, B, C, invisible)
	return ' ' .join(map(str, r))


# for N in range(1, 6):
# 	print("N=", N)
# 	for A in range(1, N+1):
# 		for B in range(1, N+1):
# 			for C in range(1, N+1):
# 				if ans(N,A,B,C) == "???":
# 					print('???')
# 					print(N,A,B,C)
# 					continue
# 				if ans(N,A,B,C) == "IMPOSSIBLE": continue
# 				m = ans(N,A,B,C).split()
# 				m = list(map(int, m))
# 				print(m)

T = int(input())
for t in range(T):
	N, A, B, C = input().split()
	N = int(N)
	A = int(A)
	B = int(B)
	C = int(C)
	print("Case #" + str(t+1) + ": " + str(ans(N, A, B, C)))
