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
from functools import lru_cache

### CODE HERE

def ans(arr):
    N = len(arr)
    need = set(range(1, N+1))

    for i in range(N):
        x = arr[i]
        while True:
            if x == 0: return "NO"
            if x in need:
                need.remove(x)
                break
            else:
                x //= 2

    return "YES"

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))
