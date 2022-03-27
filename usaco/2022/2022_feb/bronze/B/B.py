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

def LIS(arr):
    n = len(arr)
    lis = [arr[0]]
    for a in arr:
        if a > lis[-1]:
            lis.append(a)
        else:
            lis[bisect_left(lis, a)] = a
    return len(lis)

def count(A):
    N = len(A)
    deleted = [0]*(N+1)
    left = 0
    index_of = dict()
    for i, a in enumerate(A):
        index_of[a] = i

    ret = 0
    for a in range(N):
        if index_of[a] != left:
            ret += 1
        deleted[index_of[a]] = 1
        while deleted[left] == 1:
            left += 1

    return ret

def count_slow(A):
    A = A[:]
    N = len(A)
    ret = 0
    for a in range(N):
        i = A.index(a)
        if A.index(a) == 0:
            del A[i]
        else:
            ret += 1
            del A[i]
    return ret


def ans(A, B):
    index_of = dict()
    for i, b in enumerate(B):
        index_of[b] = i
    A = [index_of[a] for a in A]
    return count(A)

# tc = [1, 0, 2]
# print(count(tc))
# print(count_slow(tc))

# for _ in range(1000):
#     import random
#     tc = list(range(5))
#     random.shuffle(tc)
#     assert(count(tc) == count_slow(tc))

input()
print(ans(read_int_list(), read_int_list()))