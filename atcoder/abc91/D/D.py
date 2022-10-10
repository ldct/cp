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
from bisect import bisect_left, bisect_right
from functools import lru_cache

### CODE HERE

class StaticSortedList:
    def __init__(self, lst):
        self.lst = sorted(lst)
    def count(self, a, b):
        """Count elements in the range [a, b]"""
        return bisect_right(self.lst, b) - bisect_left(self.lst, a)
    def __repr__(self):
        return self.lst.__repr__()

def ans(A, B):
    def count_pairs(k):
        # print("count", k)
        """Count pairs i, j such that a_i + b_i has the k'th bit set"""
        T = 2**k
        sB = StaticSortedList([b % (2*T) for b in B])

        ret = 0
        for aa in A:
            a = aa % (2*T)
            ret += sB.count(T-a, 2*T-1-a)
            ret += sB.count(3*T-a, 4*T-a)

        return ret

    ret = 0
    for k in range(29):
        if count_pairs(k) % 2 == 1:
            ret += (2**k)
    return ret

if False:
    import random
    A = [random.randint(0, 2**29) for _ in range(200000)]
    B = [random.randint(0, 2**29) for _ in range(200000)]
    print(ans(A, B))
else:
    input()
    A = read_int_list()
    B = read_int_list()
    print(ans(A, B))
