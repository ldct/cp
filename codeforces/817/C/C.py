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

def ans(A, B, C):
    A = A.split(' ')
    B = B.split(' ')
    C = C.split(' ')
    cnt = Counter(A + B + C)

    score = [0, 0, 0]

    for w in A:
        if cnt[w] == 2: score[0] += 1
        if cnt[w] == 1: score[0] += 3
    for w in B:
        if cnt[w] == 2: score[1] += 1
        if cnt[w] == 1: score[1] += 3
    for w in C:
        if cnt[w] == 2: score[2] += 1
        if cnt[w] == 1: score[2] += 3

    return score

for _ in range(read_int()):
    input()
    print(*ans(input(), input(), input()))