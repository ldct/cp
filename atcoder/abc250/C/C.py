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

class IndexingList:
    """
    Like a python list, but the `index` is O(1) instead of O(n) time where
    n is the length of the list. In exchange for this speedup, an inverse
    mapping `indexes` is maintained and getting/setting items incurs an
    O(1) overhead to update the inverse mapping.
    """
    from collections import defaultdict
    def __init__(self, lst):
        self.lst = lst
        self.indexes = self.defaultdict(set)
        for i, e in enumerate(self.lst):
            self.indexes[e].add(i)
    def __getitem__(self, k):
        assert(isinstance(k, int))
        return self.lst[k]
    def __setitem__(self, k, v):
        assert(isinstance(k, int))

        old_v = self.lst[k]

        self.indexes[old_v].remove(k)
        self.indexes[v].add(k)
        self.lst[k] = v
    def __len__(self):
        return len(self.lst)
    def index(self, k, exclude=None):
        s = self.indexes[k]
        if len(s) == 0:
            return False
        for c in s:
            if c != exclude:
                return c
        return False
    def __repr__(self):
        return self.lst.__repr__()
    def __eq__(self, other):
        if isinstance(other, IndexingList): other = other.lst
        if isinstance(self, IndexingList): self = self.lst
        return self == other

### CODE HERE

N, Q = read_int_tuple()

balls = IndexingList(list(range(1, N+1)))

for _ in range(Q):
    q = read_int()

    i = balls.index(q)
    if i == len(balls)-1:
        balls[i-1], balls[i] = balls[i], balls[i-1]
    else:
        balls[i], balls[i+1] = balls[i+1], balls[i]

print(*balls)