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

def ok(N, flash):
    flash = [i-1 for i in flash]

    cf = Counter(flash)

    for k in cf:
        if cf[k] != 2: return False

    opened = [False]*N

    s = []

    for c in flash:
        if opened[c]:
            if s[-1] != c: return False
            s.pop()
            opened[c] = False
            continue
        opened[c] = True
        s += [c]

    if any(opened): return False
    return True

def ans(N, flashes):
    for flash in flashes:
        if not ok(N, flash): return False

    if N == 1:
        flashes = [[]] + flashes + [[]]
        t = 0
        for i in range(len(flashes)-1):
            if len(flashes[i]) != len(flashes[i+1]): t += 1
        return t <= 2

    if M == 1: return True

    if M >= 3: return False # exclude TC

    assert(M == 2)
    for f in flashes:
        if len(f) == 0: return True
    return flashes[0][0] == flashes[1][0]

    return N, flashes

for _ in range(read_int()):
    input()
    N, M = read_int_list()
    flashes = [read_int_list()[1:] for _ in range(M)]
    print("YES" if ans(N, flashes) else "NO")
