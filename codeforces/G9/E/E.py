#!/usr/bin/env python3

input()
A = input().split(' ')
A = [int(a) for a in A]

inversions = []

for u in range(len(A)):
    for v in range(u+1, len(A)):
        if A[u] > A[v]:
            inversions += [(-min(A[u], A[v]), u, u, v)]

inversions = sorted(inversions)

print(len(inversions))
for (_, _, u, v) in inversions:
    print(u+1, v+1)