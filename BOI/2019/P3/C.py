#!/usr/bin/env pypy3

N, S, Q, E = input().split(' ')
N = int(N)
S = int(S)
Q = int(Q)
E = int(E)

for _ in range(N-1):
	A, B, W = input().split(' ')

for _ in range(S):
	C = int(input())

R, C, M = input().split(' ')
R = int(R)
C = int(C)
M = int(M)

ocean = []
for _ in range(R):
	ocean += [input()]

M = input()

print(ans(ocean, M))