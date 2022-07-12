#!/usr/bin/env python3

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

def clean(arr):
    ret = []
    for a in arr:
        x = a
        while x > 0 and x % 2 == 0:
            x //= 2
        ret += [bin(x)]
    return sorted(ret)

def bin(x):
    return "{0:b}".format(x)

def search_prefix(p, arr):
    for i in range(len(arr)):
        if bin(arr[i]).startswith(bin(p)):
            return i

def pad (x, n):
    while len(x) != n:
        x += '0'
    return x

def ans(A, B):
    A = clean(A)[::-1]
    B = clean(B)[::-1]

    # n = max(len(x) for x in A+B)
    # A = [pad(a, n) for a in A]
    # B = [pad(b, n) for b in B]

    A = sorted(A)
    B = sorted(B)
    return A, B

for _ in range(read_int()):
    input()
    A = read_int_list()
    B = read_int_list()
    print(ans(A, B))