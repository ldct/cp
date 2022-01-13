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

def ans(N):
    ret = [0]*N
    worklist = [(-N, 0)]

    x = 1
    while len(worklist):
        size, i = heappop(worklist)
        size = -size
        split = i + (size-1) // 2

        ret[split] = x

        left_size = split - i

        if left_size > 0:
            heappush(worklist, (-left_size, i))

        right_size = size - left_size - 1

        if right_size > 0:
            heappush(worklist, (-right_size, split+1))

        x += 1

    return ret

for _ in range(read_int()):
    print(*ans(read_int()))