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

def shift(A):
    x = A[-1]
    A.pop()
    A.appendleft(x)

def ans(A):
    A = deque(A)
    ret = []

    for _ in range(len(A)):
        i = A.index(len(A))
        num_shifts = len(A) - 1 - i
        # print("num_shifts=", num_shifts)
        ret += [(len(A) - num_shifts) % len(A)]

        for _ in range(num_shifts):
            shift(A)
        A.pop()

    # print(ret, A)

    print(*ret[::-1])

for _ in range(read_int()):
    input()
    ans(read_int_list())