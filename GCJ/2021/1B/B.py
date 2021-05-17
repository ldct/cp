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

class vec2(tuple):

    @property
    def x(self): return self[0]
    @property
    def y(self): return self[1]

    def __add__(self, v): return vec2((self.x + v.x, self.y + v.y))
    def __neg__(self): return vec2((-self.x, -self.y))
    def __sub__(self, v): return self + (-v)

    def __mul__(self, v):
        if isinstance(v, vec2):
            return vec2((self.x * v.x, self.y * v.y))
        else:
            return vec2((self.x * v, self.y * v))

    def __rmul__(self, v):
        return self.__mul__(v)

from functools import lru_cache

@lru_cache(None)
def weight(n):
    if n == 0: return vec2((1,0))
    if n == -1: return vec2((0,1))
    return weight(n-1) + weight(n-2)

def compare(a, b):
    return a[0] >= b[0] and a[1] >= b[1]

def ans(U):
    total_weight = vec2((0,0))
    for i in range(len(U)):
        total_weight += weight(i+1)*U[i]

    for r in range(1, 10):
        if compare(weight(r), total_weight): return r

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
    print(ans([0,4]))
elif False:
    for _ in range(100000):
        import random
        tc = [random.randint(0, 3) for _ in range(random.randint(0, 5))]
        if sum(tc) == 0: continue
        print(tc)
        if ans(tc) != ans_slow(tc):
            print(tc, ans(tc), ans_slow(tc))
            assert(False)
else:
    T = read_int()
    for t in range(T):
        N, A, B = read_int_tuple()
        U = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans(U)))
