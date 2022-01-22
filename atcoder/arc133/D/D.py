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

def ans_slow(L, R, V):
    arr = [0]
    r = 0
    for i in range(1, R + 2):
        if i % 4 == 0:
            arr += [i]
        elif i % 4 == 1:
            arr += [1]
        elif i % 4 == 2:
            arr += [i+1]
        else:
            arr += [0]

    ret = 0

    for i in range(L-1, R+1):
        for j in range(i+1, R+1):
            if arr[i]^arr[j] == V:
                ret += 1

    return ret

print(ans_slow(*read_int_list()))