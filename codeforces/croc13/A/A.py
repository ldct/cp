#!/usr/bin/env python3

from math import gcd

def ans(A):
    g = A[0]
    for a in A:
        g = gcd(g, a)
    if g in A:
        return g
    return -1

input()
A = input().split(' ')
A = list(map(int, A))

print(ans(A))