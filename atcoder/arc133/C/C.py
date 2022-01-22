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

### CODE HERE

def ans(A, B, K):
    N = len(A)
    M = len(B)
    if (sum(A) % K) != (sum(B) % K): return -1
    A = [(M*(K-1) - a) % K for a in A]
    B = [(N*(K-1) - b) % K for b in B]
    if (sum(A) % K) != (sum(B) % K): return -1
    return N*M*(K-1) - max(sum(A), sum(B))

_, _, K = read_int_tuple()
A = read_int_list()
B = read_int_list()

print(ans(A, B, K))