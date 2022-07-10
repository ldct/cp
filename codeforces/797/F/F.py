#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import cycle, permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

def cycles(perm):
    remain = set(perm)
    result = []
    while len(remain) > 0:
        n = remain.pop()
        cycle = [n]
        while True:
            n = perm[n]
            if n not in remain:
                break
            remain.remove(n)
            cycle.append(n)
        result.append(cycle)
    return result

### CODE HERE

import math

def lcm2(a, b):
	return a*b // math.gcd(a, b)

def lcm(lst):
	ret = 1
	for l in lst:
		ret = lcm2(ret, l)
	return ret

def cost(cyc):
  cyc = ''.join(cyc)
  haystack = (cyc + cyc)[1:]
  return 1 + haystack.index(cyc)

def ans(S, P):
  P = [p-1 for p in P]
  cp = cycles(P)
  cp = [[S[i] for i in cyc] for cyc in cp]
  cp = [cost(cyc) for cyc in cp]

  return lcm(cp)

for _ in range(read_int()):
  input()
  S = input()
  P = read_int_list()
  print(ans(S, P))