#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout
from turtle import left, right

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

def ans(U, queries):
    U = [str(u) for u in U]
    sU = set(U)
    # print(U)

    left_index = dict()
    right_index = dict()

    for i in range(len(U)):
        x = U[i]
        right_index[x] = i
        if x not in left_index:
            left_index[x] = i
        
    for _a, _b in queries:
        a = str(_a)
        b = str(_b)
        if not (a in sU and b in sU):
            print("NO")
            continue
        aa = left_index[a]
        bb = right_index[b]    
        if int(aa) <= int(bb):
            print("YES")
        else:
            print("NO")

for _ in range(read_int()):
    input()
    N, K = read_int_tuple()
    U = read_int_list()
    queries = [read_int_tuple() for _ in range(K)]
    ans(U, queries)