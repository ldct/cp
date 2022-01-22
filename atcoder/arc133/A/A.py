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

def ans_greedy(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            k = arr[i]
            return [a for a in arr if a != k]
    k = max(arr)
    return [a for a in arr if a != k]

def ans_slow(arr):
    candidates = []
    for t in set(arr):
        candidates += [[a for a in arr if a != t]]
    return min(candidates)

input()
print(*ans_greedy(read_int_list()))
