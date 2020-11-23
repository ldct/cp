#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(None)
def ans(A, B, C):
    if max(A, B, C) >= 100: return 0
    T = A+B+C
    return 1 + (A/T)*ans(A+1,B,C) + (B/T)*ans(A,B+1,C) + (C/T)*ans(A,B,C+1)

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print(ans(A,B,C))