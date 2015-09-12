#!/usr/bin/env python3

from math import sqrt

N, X = input().split()
N = int(N)
X = int(X)

res = set()

for i in range(1, max(int(sqrt(X) + 1), N)):
    if X % i != 0: continue
    if X // i <= N:
        res.add((i, X//i))
        res.add((X//i, i))

print(len(res))