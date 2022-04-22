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

def split_pred(arr, pred):
	ret = []
	lazy = []

	for a in arr:
		if pred(a):
			if len(lazy):
				ret += [lazy]
			lazy = []
		else:
			lazy += [a]

	if len(lazy):
		ret += [lazy]

	return ret

### CODE HERE

def good(block):
    if len(block) == 1: return False
    return 'R' in block and 'B' in block

def ans(S):
    S = split_pred(S, lambda x: x == 'W')

    for block in S:
        if not good(block): return "NO"
    return "YES"

for _ in range(read_int()):
    input()
    print(ans(input()))