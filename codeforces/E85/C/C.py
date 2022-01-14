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

print(input())

# def ans(A, B):
#     ret = 0
#     N = len(A)
#     for i in range(N):
#         j = (i+1) % N
#         new_val = min(B[i], A[j])
#         ret += (A[j] - new_val)
#         A[j] = new_val
#     return min(A) + ret

# ret = []
# T = read_int()
# for _ in range(T):
#     A = []
#     B = []
#     for _ in range(read_int()):
#         a, b = read_int_tuple()
#         A += [a]
#         B += [b]
#     ret += [str(ans(A, B))]
# print('\n'.join(ret))
