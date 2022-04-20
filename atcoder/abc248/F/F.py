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

sys.setrecursionlimit(10000)

@lru_cache(None)
def ans(target_d, i, has_leak, two_parts):
    if target_d < 0: return 0
    if i == N-1:
        if two_parts: return 0
        if target_d == 0: return 1
        return 0

    ret = 0

    # add a complete cap
    ret += ans(target_d, i+1, False, False)
    # add a _|
    if not two_parts:
        ret += 2*ans(target_d-1, i+1, False, False)

    # add a =
    ret += ans(target_d-1, i+1, has_leak, two_parts)


    # add a _
    if (not has_leak) and (not two_parts):
        ret += 2*ans(target_d-2, i+1, True, True)

    return ret % MODULUS

if True:
    N, MODULUS = read_int_tuple()
else:
    N, MODULUS = 16, 999999937

ret = []
for d in range(1, N):
    a = ans(d-1, 0, True, True)
    b = ans(d, 0, False, False)
    ret += [(a+b) % MODULUS]

print(*ret)

# print(ret)
if ret == 16:
    assert(" ".join(map(str, ret)) == "46 1016 14288 143044 1079816 6349672 29622112 110569766 330377828 784245480 453609503 38603306 44981526 314279703 408855776")