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

def rle_block(arr):
    last_e = None
    last_n = 0
    last_i = -1

    ret = []
    for i, c in enumerate(arr):
        if c != last_e:
            if last_n > 0:
                ret += [(last_i, [last_e]*last_n)]
            last_e = c
            last_n = 1
            last_i = i
        else:
            last_n += 1

    ret += [(last_i, [last_e]*last_n)]
    return ret

def ans_seg(l):
    if l == 2: return 0
    if l == 3: return 1
    return l - 3

def ans(arr):
    arr = [(a, len(b)) for (a, b) in rle_block(arr) if len(b) > 1]
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        _, l = arr[0]
        return ans_seg(l)

    (a, l_a) = arr[0]
    (b, l_b) = arr[-1]
    assert(a != b)

    end = b + l_b
    l = end - a
    return ans_seg(l)


    return arr

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))