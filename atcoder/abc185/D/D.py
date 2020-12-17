#!/usr/bin/env pypy3

import math

N, M = input().split()
N = int(N)
A = list(map(int, input().split()))
A = sorted(set(A + [0, N+1]))
gaps = []
for i in range(len(A)-1):
    gap = A[i+1] - A[i] - 1
    if gap > 0:
        gaps += [gap]

if len(gaps) == 0:
    print(0)
else:
    K = min(gaps)

    ret = 0
    for gap in gaps:
        ret += math.ceil(gap / K)

    print(ret)