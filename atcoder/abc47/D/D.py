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

def ans(A):
    def mp(low, high):
        l = high - low
        if l <= 1: return 0
        mid = (low + high) // 2
        return max(
            mp(low, mid),
            mp(mid, high),
            0,
            max(A[mid:high]) - min(A[low:mid])
        )

    def count(arr, target):
        ret = 0
        for e in arr:
            if e == target:
                ret += 1
        return ret

    def cost(low, high, max_profit):
        # cost to make every profit <= max_profit
        l = high - low
        if l <= 1: 
            # print(f"cost({A[low:high]}) = 0")
            return 0
        mid = (low + high) // 2

        ret = cost(low, mid, max_profit) + cost(mid, high, max_profit)

        left_min = min(A[low:mid])
        right_max = max(A[mid:high])

        curr_profit = right_max - left_min

        if curr_profit > max_profit:

            ret += min(
                count(A[low:mid], left_min),
                count(A[mid:high], right_max)
            )

        # print(f"cost({A[low:high]}) = {ret}")
        return ret
        

    cp = mp(0, len(A))

    # print("max_profit=", cp-1)
    return cost(0, len(A), cp-1)



if True:
    input()
    A = read_int_list()
    print(ans(A))

