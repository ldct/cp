#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


from sys import stdin, stdout
import bisect

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from heapq import *

class BestIntervals:
    def done(self):
        for k in range(K+1):
            self.lookup[k].sort()

    def __init__(self, K):
        self.points = []

        self.min_idx = []
        self.lookup = []
        for _ in range(K+1):
            self.lookup += [[]]
            self.min_idx += [0]
        self.min_i = -1
        self.K = K

    def set_min_i(self, target):
        assert(target >= self.min_i)
        self.min_i = target

    def add_point(self, b):
        self.points += [b]
        j = len(self.points)-1
        for i in range(len(self.points)):
            total = b - self.points[i]
            if total > self.K: continue
            self.lookup[total] += [(j - i)*10**4 + i]

    def best(self, k):
        assert k <= self.K
        while self.min_idx[k] < len(self.lookup[k]):
            r = self.lookup[k][self.min_idx[k]]
            i = r % 10**4
            score = r // (10**4)
            if i < self.min_i:
                self.min_idx[k] += 1
                continue
            else:
                return score

        return float("inf")

def ans_one(K, B):
    best = float("inf")

    prefixes = [0]
    for b in B: prefixes += [prefixes[-1] + b]

    for i in range(len(prefixes)):
        j = bisect.bisect_left(prefixes, prefixes[i] + K)
        if j < len(prefixes) and prefixes[j] == prefixes[i] + K:
            best = min(best, j - i)

    return best

def size(p):
    return p[1] - p[0]

def intersects(a, b):
    (i, j) = a
    (k, l) = b
    if j < k: return False
    if i > l: return False
    return True

def ok(i1, i2):
    if intersects(i1, i2): return False
    [i1, i2] = sorted([i1, i2])
    return i1[1] < i2[0]


def ans_slow(K, B):
    best = ans_one(K, B)

    p = [0]
    for b in B: p += [p[-1] + b]

    bi = BestIntervals(K)
    for x in p: bi.add_point(x)
    bi.done()

    for j in range(len(p)):
        bi.set_min_i(j+1)

        for i in range(j):
            target_sum = K - (p[j] - p[i])
            if target_sum < 0: continue

            # print("searching for", bi.min_i, target_sum)
            r = bi.best(target_sum)
            if r < float("inf"):
                best = min(best, j-i + r)

    if best == float("inf"): return -1
    return best


def ans(K, B):
    best = ans_one(K, B)

    p = [0]
    for b in B: p += [p[-1] + b]

    bi = BestIntervals(K)
    for x in p: bi.add_point(x)

    for j in range(len(p)):
        bi.set_min_i(j+1)

        for i in range(j):
            target_sum = K - (p[j] - p[i])
            if target_sum < 0: continue

            # print("searching for", bi.min_i, target_sum)
            r = bi.best(target_sum)
            if r < float("inf"):
                best = min(best, j-i + r)

    if best == float("inf"): return -1
    return best


if False:
    K, B = 4, [1, 2, 3, 2, 1]
    print("ans_slow=", ans_slow(K, B))
    print("ans=", ans(K, B))
elif False:
    import random
    for _ in range(100000):
        K = random.randint(1,100)
        B = [random.randint(1, K) for _ in range(20)]
        if not (ans(K, B) == ans_slow(K, B)):
            print(K, B)
            assert(False)
    print("done")
elif False:
    import random
    for _ in range(1):
        K = random.randint(5*10**5, 10**6)
        B = [random.randint(1, 2) for _ in range(5000)]
        print(ans(K, B))
else:
    T = int(input())
    for t in range(T):
        N, K = read_int_tuple()
        B = read_int_list()
        print("Case #" + str(t+1) + ": " + str(ans(K, B)))
