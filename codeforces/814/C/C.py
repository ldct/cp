#!/usr/bin/env python3

import enum
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

class RangeFreq():
    def __init__(self, arr):
        self.store = defaultdict(list)
        for i, a in enumerate(arr):
            self.store[a] += [i]
    def query(self, left, right, element):
        a = bisect_left(self.store[element], left)
        b = bisect_right(self.store[element], right)
        return b - a

def ans(A, queries):

    winner_idx = None

    for i, a in enumerate(A):
        if a == len(A):
            winner_idx = i+1

    win_res = []
    def win(p):
        p += 1
        win_res.append(p)
        

    N = len(A)
    A = deque(enumerate(A))

    while True:
        if A[0][1] == N:
            break

        a = A.popleft()
        b = A.popleft()

        if a[1] > b[1]:
            win(a[0])
            A.appendleft(a)
            A.append(b)
        else:
            win(b[0])
            A.append(a)
            A.appendleft(b)

    engine = RangeFreq(win_res)

    for e, rhs in queries:
        ret = engine.query(0, rhs-1, e)
        if e == winner_idx:
            g = (rhs - len(win_res))
            if g > 0:
                ret += g
        print(ret)

    # print()

for _ in range(read_int()):
    n, q = read_int_list()
    A = read_int_list()
    queries = [read_int_tuple() for _ in range(q)]
    ans(A, queries)