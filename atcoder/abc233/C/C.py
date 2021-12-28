#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

N, X = read_int_list()
balls = []
for _ in range(N):
    balls += [read_int_list()[1:]]

ret = 0

for s in product(*balls):
    r = 1
    for c in s:
        r *= c
    if r == X: ret += 1

print(ret)