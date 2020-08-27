#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()
	
def majority(arr):
	num_0 = 0
	num_1 = 0

	for c in arr:
		assert c in "01?"

		if c == '0':
			num_0 += 1
		if c == '1':
			num_1 += 1

	if num_0 > num_1:
		return '0'
	return '1'

def ans(N, S):
	mid = (2*N-1) // 2
	# print("mid=", mid)
	return S[mid]*N

T = int(input())
for t in range(T):
	N = int(input())
	s = input()
	print(ans(N, s))