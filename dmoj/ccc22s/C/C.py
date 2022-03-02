#!/usr/bin/env pypy3

import io, os
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

def score2(N, K):
    K = min(N, K)
    return (K * (2*N - K + 1)) // 2

def ans(N, K, target_score):

    if N == 1:
        if target_score == 1: return [1]
        return [-1]
    if not (N <= target_score <= score2(N, K)): return [-1]

    for head in range(1, N+1):
        tail = N-head
        low = score2(head, K) + tail
        high = low
        if tail > 0:
            high += min(K-1, head-1)

        if low <= target_score <= high:
            # print("head=", head)
            ret = [0]
            while len(ret) != head:
                ret += [(ret[-1] + 1) % K]
            gap = target_score - low
            # print("gap=", gap)
            tail_val = ret[head - gap - 1]
            ret += [tail_val]*tail
            return [x+1 for x in ret]

    assert(False)

def evaluate(arr):
    ret = 0
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            sub = arr[i:j]
            if len(sub) == len(set(sub)):
                ret += 1
    return ret

# print(ans(2, 2, 3))

# for N in range(1, 16):
#     for K in [2]:
#         for target_score in range(1, 1000):
#             r = ans(N, K, target_score)
#             if r[0] != -1:
#                 if not (target_score == evaluate(r)):
#                     print(N, K, target_score)

print(*ans(*read_int_tuple()))