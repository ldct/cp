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

def is_subsequence(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = find(haystack, c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

### CODE HERE

def score(seq):
    ret = 0
    for i in range(len(seq)-1):
        ret += abs(seq[i+1] - seq[i])
    return ret

def good(p):
    return p[0] <= p[1]

def ans_slow(X, A):
    big = A + list(range(1, X+1))

    ret = float("inf")
    for p in permutations(big):
        if not is_subsequence(A, p): continue
        ret = min(ret, score(p))

    return ret

def ans(X, A):

    low = min(A)
    high = max(A)

    if X < low:
        need_to_insert = [(1, X)]
    else:
        need_to_insert = [(1, low-1)]
        if high < X:
            need_to_insert += [(high+1, X)]

    need_to_insert = [r for r in need_to_insert if good(r)]

    bag = [low, high]
    for p in need_to_insert:
        bag += p

    ret = score(A)
    for a, b in need_to_insert:
        ret += b-a
        if a <= b < low <= high:
            ret += min(A[0] - b, A[-1] - b, 2*(low - b) + (b-a))
        elif low <= high < a <= b:
            ret += min(a - A[0], a - A[-1], 2*(a - high) + (b-a))
        else:
            assert(False)
    return ret

    r = ret + best(bag) - score([low, high])
    return r, A, need_to_insert
    return ret, (low, high), bag, best(bag)

if False:
    X = 2
    A = [5, 3, 5]
    print(ans_slow(X, A))
    print(ans(X, A))
elif False:
    import random
    for X in range(1, 5):
        for _ in range(1000):
            A = [random.randint(1, 5) for _ in range(4)]
            if not (ans(X, A) == ans_slow(X, A)):
                print(X, A)
else:
    for _ in range(read_int()):
        N, X = read_int_tuple()
        A = read_int_list()
        print(ans(X, A))