#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

from bisect import bisect_left

def LIS(arr):
    n = len(arr)
    lis = [arr[0]]
    for a in arr:
        if a > lis[-1]:
            lis.append(a)
        else:
            lis[bisect_left(lis, a)] = a
    return len(lis)

def cross_free(N, pairs):
    M = len(pairs)

    A = [[] for _ in range(N)]

    for a,b in pairs:
        A[a].append(b)

    for i in range(N):
        A[i].sort(reverse=True)

    B = []

    for i in range(N):
        for j in A[i]:
            B.append(j)

    return LIS(B)



N = read_int()
P = read_int_list()
Q = read_int_list()

QI = dict()
for i, q in enumerate(Q):
    QI[q] = i

pairs = []

for j in range(N):
    p = P[j]
    while True:
        if p > N: break
        i = QI[p]
        pairs += [(i, j)]
        p += P[j]

# print("found pairs", len(pairs))
print(cross_free(N, pairs))