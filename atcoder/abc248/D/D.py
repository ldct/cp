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

### CODE HERE

input()
A = read_int_list()
queries = defaultdict(set)


ordered_queries = []

ans = dict()

for _ in range(read_int()):
    l, r, x = read_int_tuple()
    l -= 1
    r -= 1
    queries[l].add(x)
    queries[r+1].add(x)

    ordered_queries += [(l, r, x)]

freq = defaultdict(int)
for i, a in enumerate(A):
    freq[a] += 1

    for q in queries[i+1]:
        ans[(i+1, q)] = freq[q]
        # print(i+1, q)
        # print(f"freq[0:{i+1}][q] = {freq[q]}")
        # assert(Counter(A[0:i+1])[q] == freq[q])

def get_ans(i, x):
    if i == 0: return 0
    return ans[i, x]
for l, r, x in ordered_queries:
    print(get_ans(r+1,x) - get_ans(l,x))