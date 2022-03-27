#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def gt(A, B):
    a_win = 0
    b_win = 0

    for a in A:
        for b in B:
            if a > b:
                a_win += 1
            if a < b:
                b_win += 1

    return a_win > b_win

def ans(arr):
    A = arr[:4]
    B = arr[4:]
    if gt(B, A):
        A, B = B, A
    if not gt(A, B):
        return "no"

    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    C = [a, b, c, d]
                    if gt(B, C) and gt(C, A): return "yes"

    return "no"

for _ in range(read_int()):
    print(ans(read_int_list()))