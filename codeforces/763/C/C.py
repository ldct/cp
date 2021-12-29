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

def ans(_arr):

    @lru_cache(None)
    def ok(k):
        arr = _arr[:]
        old_arr = _arr[:]

        for i in range(len(arr)-1, 1, -1):

            if arr[i] < k: return False
            d = (arr[i] - k) // 3
            d = min(d, old_arr[i] // 3)

            arr[i-2] += 2*d
            arr[i-1] += d
            arr[i] -= 3*d

        for x in arr:
            assert(x >= 0)
            if x < k: return False

        return True

    low = 0
    high = 10**9+1

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for i in range(low, low+10):
        if not ok(i):
            return i-1


for _ in range(read_int()):
    input()
    print(ans(read_int_list()))