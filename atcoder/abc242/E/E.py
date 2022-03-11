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

MODULUS = 998244353

def ans(S):
    S = [ord(c) - ord('A') for c in S]
    half = (len(S)+1)//2
    ret = 0
    for i in range(half):
        j = len(S)-1-i
        # print("add", S[i]*26**(half-i-1))
        ret += S[i]*26**(half-i-1)
        # ret %= MODULUS
    return ret

for _ in range(read_int()):
    input()
    print(ans(input()))