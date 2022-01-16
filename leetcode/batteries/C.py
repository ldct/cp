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

class Solution:
    def maxRunTime(self, n, batteries):
        batteries.sort(reverse=True)
        def ok(t):
            B = batteries[0:n]
            extra = sum(batteries[n:])

            need = 0
            for b in B:
                if t - b > 0:
                    need += t - b

            return need <= extra

        low = 1
        high = sum(batteries)+1

        assert(ok(low))
        assert(not(ok(high)))

        while high - low > 2:
            mid = (low + high) // 2
            if ok(mid):
                low = mid
            else:
                high = mid

        for i in range(low, low+10):
            if not ok(i):
                return i-1

s = Solution()
print(s.maxRunTime(2, [3,5,10,10]))