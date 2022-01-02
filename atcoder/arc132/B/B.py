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

def ans_march(p, n):
    if (p[0], p[1]) == (0, 1): return 0
    ret = 0
    i, j = 0, 1
    for ret in range(2*n):
        ret += 1
        i += 1
        j += 1
        i %= n
        j %= n
        if (p[i], p[j]) == (0, 1): return ret
    return float("inf")

def ans_march_rev(p, n):
    if (p[0], p[1]) == (n-1, n-2): return 1
    ret = 0
    i, j = 0, 1
    for ret in range(2*n):
        ret += 1
        i += 1
        j += 1
        i %= n
        j %= n
        if (p[i], p[j]) == (n-1, n-2): return ret+1
    return float("inf")

def ans(p):
    p = [x-1 for x in p]
    ret = min(
        ans_march(p, len(p)),
        ans_march_rev(p, len(p))
    )
    p.reverse()
    ret = min(
        ret,
        1+ans_march(p, len(p)),
        1+ans_march_rev(p, len(p))
    )
    return ret


input()
print(ans(read_int_list()))