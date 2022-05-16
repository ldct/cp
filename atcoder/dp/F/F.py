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

def find(arr, x, start):
    for i in range(start, len(arr)):
        if arr[i] == x: return i
    return -1

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

def subsequences(S):
    ret = []
    for indices in subsets(range(len(S))):
        ret += [[S[i] for i in indices]]
    return ret

def is_subsequence(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = find(haystack, c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

def lcs2_slow(A, B):
    A = list(A)
    B = list(B)
    ret = ""
    for a in subsequences(A):
        if is_subsequence(a, B):
            if len(a) > len(ret):
                ret = a
    return ret

def lcs2(A, B):
    def dp(i, j):
        if i >= len(A): return 0
        if j >= len(B): return 0

        ret = 0
        if A[i] == B[j]: ret = max(ret, 1+dp(i+1, j+1))
        ret = max(ret, dp(i+1, j))
        ret = max(ret, dp(i, j+1))

        return ret
    return dp(0, 0)

### CODE HERE

print(lcs2(input(), input()))