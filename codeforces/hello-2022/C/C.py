#!/usr/bin/env pypy3

from sys import stdin, stdout

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def fprint(*args):
	print(*args, flush=True)

def query(x):
    fprint(f"? {x}")
    return int(input())

def get_cycle(x):
    ret = []
    seen = set()

    while True:
        y = query(x)
        if y in seen:
            return ret
        ret += [y]
        seen.add(y)

def choose(s):
    for c in s:
        return c
    assert(False)

def guess(N, cycles):
    ret = dict()
    for cycle in cycles:
        ext = cycle[:] + [cycle[0]]
        for i in range(len(ext)-1):
            ret[ext[i]] = ext[i+1]

    p = [str(ret[k]) for k in range(1, N+1)]
    fprint("! " + " ".join(p))

for _ in range(int(input())):
    N = int(input())
    unseen = set(range(1, N+1))

    cycles = []

    while len(unseen):
        x = choose(unseen)
        c = get_cycle(x)
        cycles += [c]
        for t in c:
            unseen.remove(t)

    guess(N, cycles)
