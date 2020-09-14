#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(N, A, L):
	unlocked = []
	for i in range(N):
		if L[i] == 0:
			unlocked += [A[i]]
	unlocked = sorted(unlocked)[::-1]

	j = 0
	
	for i in range(N):
		if L[i] == 0:
			A[i] = unlocked[j]
			j += 1
	
	print(*A)

T = int(input())
for t in range(T):
	N = int(input())
	A = list(map(int, input().split()))
	L = list(map(int, input().split()))

	assert(N == len(A))
	assert(N == len(L))

	ans(N, A, L)