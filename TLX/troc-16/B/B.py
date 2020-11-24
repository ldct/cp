#!/usr/bin/env pypy3

N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
A = sorted(A)
A = [a - 1 for a in A]

A += [a + M for a in A]

i = 0
j = N - 1

ret = 4*M

while j < len(A):
    ret = min(ret, A[j] - A[i])
    i += 1
    j += 1

print(ret)