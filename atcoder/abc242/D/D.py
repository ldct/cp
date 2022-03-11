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

def expand(c):
    if c == "A": return "BC"
    if c == "B": return "CA"
    if c == "C": return "AB"
    assert(False)

def cyc(c):
    if c == "A": return "ABC"
    if c == "B": return "BCA"
    if c == "C": return "CAB"
    assert(False)

def f(c, t, k):
    if k == 0:
        return cyc(c)[t % 3]
    if t == 0:
        assert(k == 0)
        return c
    if t > 64:
        prev = f(c, t-1, k // 2)
        return expand(prev)[k % 2]

    B = 2**(t-1)
    if k < B:
        prev = f(c, t-1, k // 2)
        return expand(prev)[k % 2]
    else:
        prev = f(c, t-1, k // 2)
        return expand(prev)[k % 2]

def F(S, t, k):
    if t == 0: return S[k]
    if t > 64:
        K = 0
        return f(S[K], t, k)
    B = 2**t
    K, k = k // B, k % B

    # while k >= B:
    #     K += 1
    #     k -= B

    return f(S[K], t, k)

# import random
# S = ''.join(random.choice("ABC") for _ in range(10**5))
# print(F(S, 3, 10**15))

S = input()
for _ in range(read_int()):
    t, k = read_int_tuple()
    print(F(S, t, k-1))


# print(f("A", 2, 1))
# for i in range(12):
#     print(F("ABC", 2, i))
