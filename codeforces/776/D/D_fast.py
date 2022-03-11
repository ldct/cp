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

class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1

class IndexingDelList:
    """
    A list with fast index and del operations
    Note: del is with indexes of the original
    However, get/set are not supported
    """
    from collections import defaultdict
    def __init__(self, A):
        self.ones = FenwickTree([1]*len(A))
        self.A = list(A)
        self.index_of = dict()
        for i, a in enumerate(A):
            self.index_of[a] = i
        self.total_len = len(A)

    def index(self, n):
        return self.ones.query(self.index_of[n])


    def __getitem__(self, k):
        # not implemented, could do some binary search
        assert(False)
    def __setitem__(self, k, v):
        assert(False)
    def __len__(self):
        return self.total_len

    def remove(self, a):
        self.total_len -= 1
        idx = self.index_of[a]
        self.ones.update(idx, -1)

def ans(A):
    N = len(A)
    A = IndexingDelList([a-1 for a in A])
    last = N
    ret = []
    for n in range(N-1, -1, -1):
        r = A.index(n)
        gap = (r + len(A) - last + 1) % len(A)
        ret += [gap]
        last = r
        A.remove(n)
    return ret[::-1]

print(ans(range(1, 1000000))[0])

for _ in range(read_int()):
    input()
    print(*ans(read_int_list()))
