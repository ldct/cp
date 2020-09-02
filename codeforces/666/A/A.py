#!/usr/bin/env pypy3
	
N = int(input())
A = list(map(int, input().split()))

if N == 1:
	import sys
	print(1, 1)
	print(0)
	print(1, 1)
	print(0)
	print(1, 1)
	print(-A[0])
	sys.exit(0)
	
# first operation

to_add = []
for i in range(N-1):
	to_add += [A[i]*(N-1)]
print(1, N-1)
print(*to_add)

for i in range(N-1):
	A[i] += to_add[i]

# second operation

to_add = N-A[-1]
if to_add == 0:
	to_add = N
print(N, N)
print(to_add)

A[-1] += to_add

# print(A)

# third operation
to_add = []
for a in A:
	assert(a % N == 0)
	to_add += [-a]
print(1,N)
print(*to_add)
