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

def ans(A, B):
    ret = float("inf")
    A.sort()
    B.sort()

    for a in A:
        i = bisect_left(B, a)
        for j in [i-1, i, i+1]:
            try:
                ret = min(ret, abs(a - B[j]))
            except:
                pass
    return ret

input()
A = read_int_list()
B = read_int_list()
print(ans(A, B))