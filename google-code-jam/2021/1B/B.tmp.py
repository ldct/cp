#!/usr/bin/env python3

from __future__ import division, print_function

import itertools
import sys
import array
from collections import Counter

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from heapq import *

class FreqHeap():
    def __init__(self):
        self.heap = []
    def __len__(self):
        (e, count) = heappop(self.heap)
        while len(self.heap) and self.heap[0][0] == e:
            (_, nc) = heappop(self.heap)
            count += nc
        heappush(self.heap, (e, count))
        return len(self.heap)
    def pop(self):
        if len(self.heap) == 0: return None
        (e, count) = heappop(self.heap)
        while len(self.heap) and self.heap[0][0] == e:
            (_, nc) = heappop(self.heap)
            count += nc
        return (e, count)
    def pretty(self):
        ret = []
        for (e, count) in self.heap:
            ret += [e]*count
        print(ret)

    def push(self, e, count):
        if count == 0: return
        heappush(self.heap, (e, count))

from functools import lru_cache

@lru_cache(None)
def weight(n):
    if n <= 3: return n
    return weight(n-1) + weight(n-2)

def ans(U):
    while U[0] > U[1]:
        U[0] -= 1
        U[1] += 1
    total_weight = 0
    for i in range(len(U)):
        total_weight += weight(i+1)*U[i]

    for r in range(1, 10000000):
        if weight(r) >= total_weight: return r

def nexts(A):
    ret = []
    for i in range(len(A)):
        new_A = list(A)
        new_A += [A[i]-1,A[i]-2]
        del new_A[i]
        new_A = [a for a in new_A if a > 0]
        if len(new_A):
            ret += [tuple(sorted(new_A))]
    return ret

def alls(A):
    ret = set([A])
    for _ in range(1000):
        add = set()
        for r in ret:
            for n in nexts(r):
                add.add(tuple(sorted(n)))

        if add.issubset(ret): break

        for a in add: ret.add(a)

    return ret

def subset(l1, l2):
    from collections import defaultdict
    freqs = defaultdict(int)
    for x in l2: freqs[x] += 1
    for x in l1:
        if freqs[x] == 0: return False
        freqs[x] -= 1
    return True

def ans_slow(A):
    reqs = []
    for i in range(len(A)):
        reqs += [i+1]*A[i]
    reqs = tuple(sorted(reqs))

    for r in range(1, 100):
        for a in alls((r,)):
            if subset(reqs, a):
                return r

# for i in range(1, 25):
#     print(i, ans_slow([i]))

if False:
    print(ans([2,0,0]), ans_slow([2,0,0]))
elif False:
    for _ in range(100000):
        import random
        tc = [random.randint(0, 20) for _ in range(20)]
        if sum(tc) == 0: continue
        ans(tc)
        # if ans(tc) != ans_slow(tc):
        #     print(tc, ans(tc), ans_slow(tc))
        #     assert(False)
else:
    T = read_int()
    for t in range(T):
        N, A, B = read_int_tuple()
        U = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans(U)))
