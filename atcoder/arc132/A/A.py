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

input()
R = read_int_list()
C = read_int_list()
ret = ""
for _ in range(read_int()):
    r, c = read_int_tuple()
    r -= 1
    c -= 1
    r = R[r]
    c = C[c]
    if r + c >= len(R)+1:
        ret += "#"
    else:
        ret += "."
print(ret)