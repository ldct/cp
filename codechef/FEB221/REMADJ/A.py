#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd, sqrt
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def partitions(arr):
    ret = []
    n = len(arr)

    for partition_index in range(2 ** (n-1)):

        # current partition, e.g., [['a', 'b'], ['c', 'd', 'e']]
        partition = []

        # used to accumulate the subsets, e.g., ['a', 'b']
        subset = []

        for position in range(n):

            subset.append(arr[position])

            # check whether to "break off" a new subset
            if 1 << position & partition_index or position == n-1:
                partition.append(subset)
                subset = []

        ret += [partition]
    return ret

def divisors(n):
    if n == 0:
        yield 0
        return

    if n < 0: n = -n

    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def cost_slow(arr, target):
    candidates = []
    for p in partitions(arr):
        pp = list(map(sum, p))
        if set(pp) == set([target]): candidates += [len(p)]
    if len(candidates) == 0: return -1
    return max(candidates)

def cost(arr, target):
    ret = 0
    csum = 0
    for t in arr:
        csum += t
        if csum == target:
            ret += 1
            csum = 0
    if csum == 0: return ret
    if target == 0:
        if sum(arr) == 0: return 1
        return -1
    if csum % target == 0:
        return ret - abs(csum) // abs(target)
    if sum(arr) == target:
        return 1

    return -1

def ans(arr):
    total = sum(arr)
    if total == 0:
        return len(arr) - cost(arr, 0)

    D = list(divisors(total))
    ret = []
    for d in D:
        ret += [cost(arr, d), cost(arr, -d)]
    return len(arr) - max(ret)

def ans_slow(arr):
    total = sum(arr)
    if total == 0:
        return len(arr) - cost_slow(arr, 0)

    D = list(divisors(total))
    ret = []
    for d in D:
        ret += [cost_slow(arr, d), cost_slow(arr, -d)]

    M = max(ret)
    return len(arr) - max(ret)

tc = [1, 1, -1]
tc = [1, 1, 1, -1]
tc = [1, 1, 1, 1, -2]
# print(ans_slow(tc))
# print(ans(tc))
# assert(ans(tc) == ans_slow(tc))

# for _ in range(1000000):
#     import random
#     tc = [random.randint(-2, 2) for _ in range(random.randint(1, 5))]
#     if not (ans(tc) == ans_slow(tc)):
#         print(tc)

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))