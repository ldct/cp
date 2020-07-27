#!/usr/bin/env pypy3

from collections import Counter

def ans(C):
    c = Counter(C)
    for k in c:
        assert(k in "AB")

    a = c['A']
    b = c['B']
    if abs(a - b) == 1: return 'Y'
    return 'N'

T = int(input())

for t in range(T):
    N = int(input())
    C = input()
    print(f"Case #{t+1}: {ans(C)}")