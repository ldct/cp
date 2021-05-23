#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from math import comb
from functools import lru_cache

@lru_cache(None)
def ans(A, B, K):
    if K == 0: return "a"*A + "b"*B
    if A == 0: return "b" * B
    if B == 0: return "a" * A
    H = comb(A+B-1, A-1)
    if K <= H-1:
        return "a" + ans(A-1, B, K)
    else:
        return "b" + ans(A, B-1, K-H)

### CODE HERE

A, B, K = read_int_tuple()
K -= 1

print(ans(A, B, K))