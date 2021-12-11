#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

class BCCounter:
    def __init__(self, N=2*10**5+10):
        self.N = N
        self.freqs = [0]*N
        self.eligible = set()

    def get_eligible(self):
        for e in self.eligible:
            return e

    def update(self, idx):
        f = self.freqs[idx]
        if f in [0, 1] and idx in self.eligible:
            self.eligible.remove(idx)
        elif f == 2:
            self.eligible.add(idx)

    def inc(self, idx):
        self.freqs[idx] += 1
        self.update(idx)

    def decr(self, idx):
        self.freqs[idx] -= 1
        self.update(idx)

N, M = read_int_tuple()
cylinders = []
for _ in range(M):
    input()
    cylinders += [read_int_list()[::-1]]

cylinder_of = defaultdict(list)

for c in range(len(cylinders)):
    cylinder = cylinders[c]
    for b in cylinder:
        cylinder_of[b] += [c]

# print(cylinder_of)

counter = BCCounter(N+1)

for c in cylinders:
    counter.inc(c[-1])

# print(cylinder_of)

to_remove = N
while to_remove:
    if len(counter.eligible) == 0:
        print("No")
        import sys
        sys.exit(0)
    e = counter.get_eligible()
    i, j = cylinder_of[e]
    # print("removing", e, "from", i, j)
    cylinders[i].pop()
    if len(cylinders[i]): counter.inc(cylinders[i][-1])
    cylinders[j].pop()
    if len(cylinders[j]): counter.inc(cylinders[j][-1])
    counter.decr(e)
    counter.decr(e)
    to_remove -= 1

print("Yes")
