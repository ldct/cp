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

def ans_same(a, b):
    N = len(a)
    if a.count('1') != b.count('1'): return float("inf")
    ret = 0
    for i in range(N):
        if a[i] != b[i]: ret += 1
    return ret

def ans_diff(a, b):
    N = len(a)
    x = a.count('1')
    y = N - x

    if b.count('1') != y + 1: return float("inf")
    ret = 0
    for i in range(N):
        if a[i] == b[i]: ret += 1
    return ret

def ans(a, b):
    ret = min(ans_diff(a, b), ans_same(a, b))
    if ret == float("inf"): ret = -1
    return ret

for _ in range(read_int()):
    input()
    a = input()
    b = input()
    print(ans(a, b))