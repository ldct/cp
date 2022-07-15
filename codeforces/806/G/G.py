#!/usr/bin/env python3

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

def ans(K, A):
    ret = 0
    def cost():
        return sum([(a//2) for a in A])

    for i in range(len(A)):
        if cost() < K:
            A = [a//2 for a in A]
            ret += A[i]
            A[i] = 0
        else:
            ret += A[i]
            ret -= K
            A[i] = 0

    return ret

for _ in range(read_int()):
    N, K = read_int_list()
    A = read_int_list()
    print(ans(K, A))