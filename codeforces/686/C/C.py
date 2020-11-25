#!/usr/bin/env python3

from collections import Counter

def compress(A):
    ret = []
    for a in A:
        if len(ret) == 0 or a != ret[-1]:
            ret += [a]
    return ret

def ans(A):
    A = compress(A)
    sA = set(A)

    N = len(A)
    if N == 1: return 0

    cA = Counter(A)

    for v in sA:
        cA[v] += 1

    cA[A[0]] -= 1
    cA[A[-1]] -= 1

    return min([cA[v] for v in sA])

    return cA


for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    print(ans(A))
