#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A):
	m = min(A)
	sA = sorted(A)

	for i in range(len(A)):
		if A[i] == sA[i]: continue
		if A[i] % m != 0: return 'NO'
	
	return 'YES'


T = int(input())
for t in range(T):
	input()
	A = input().split()
	A = list(map(int, A))
	print(ans(A))