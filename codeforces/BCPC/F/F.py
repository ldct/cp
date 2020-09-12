#!/usr/bin/env pypy3

def contains(covered, x):
    for (a, b) in covered:
        if a <= x <= b: return True
    return False
    
N, U = input().split()
N = int(N)
U = int(U)

covered = []

for _ in range(U):
    a, b = input().split()
    a = int(a)
    b = int(b)

    covered += [(a, b)]

covered = sorted(covered + [(-1, 0)])

import sys

for (a, b) in covered:
    if not contains(covered, b+1):
        print(b+1)
        sys.exit(0)

assert(False)       