#!/usr/bin/env pypy3

N, M = input().split()
N = int(N)
M = int(M)

A = list(map(int, input().split()))

import array
leftmost_idx = array.array('i', [-1]*10**6)
rightmost_idx = array.array('i', [-1]*10**6)

for i, a in enumerate(A):
    if leftmost_idx[a] == -1:
        leftmost_idx[a] = i
    rightmost_idx[a] = i

ret = 0

for _ in range(M):
    a, b = input().split()
    a, b = int(a), int(b)
    if (rightmost_idx[a] != -1) and (leftmost_idx[b] != -1):
        ret = max(ret, rightmost_idx[b] - leftmost_idx[a] + 1)

print(ret)
