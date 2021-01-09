#!/usr/bin/env python3

from collections import Counter

def ans(A):
    cA = Counter(A)
    bad = set()

    for a in set(A):
        p = 2*a
        while p < 10**6 + 10:
            bad.add(p)
            p += a

    ret = 0
    for a in A:
        if a not in bad and cA[a] == 1:
            ret += 1

    return ret

input()
A = input().split(' ')
A = [int(x) for x in A]

print(ans(A))