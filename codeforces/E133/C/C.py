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

def f(row0, row1):
    ret = [row0[0]] + row1[:]
    row0 = row0[1:]
    ret += row0[::-1]
    return ret

def g(row0, row1):
    arr = list(zip(row0, row1))

    ret = []
    for i, row in enumerate(arr):
        if i % 2 == 0:
            ret += row
        else:
            ret += row[::-1]
    
    return ret


def solve(arr):
    t = 0
    for i in range(len(arr)):
        if arr[i] != 0 and arr[i] - t >= 0:
            t += (arr[i] + 1 - t)
        # print(f"visit i={i} at t={t}")
        t += 1
    return t-1

def ans(row0, row1):

    order1 = row0 + row1[::-1]

    order2 = f(row0, row1)

    order3 = g(row0, row1)

    return (order1, order2, order3)

    return min(
        solve(order1), 
        solve(order2), 
        solve(order3)
    )

if True:
    print(ans(["a", "b", "c"], ["d", "e", "f"]))
else:
    for _ in range(read_int()):
        input()
        print(ans(read_int_list(), read_int_list()))