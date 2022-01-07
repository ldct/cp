#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
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

def prefixes(arr):
    ret = [0]
    for a in arr:
        ret += [ret[-1] + a]
    return ret

def ans(arr):
    if sum(arr) % 3 != 0:
        return 0

    target = sum(arr) // 3

    front = prefixes(arr)
    back = prefixes(arr[::-1])

    fi = []
    for i in range(len(front)):
        if front[i] == target:
            fi += [i]

    bj = []
    for j in range(len(back)):
        if back[j] == target:
            bj += [len(arr) - j]

    ret = 0

    fi = [i for i in fi if 0 < i < len(arr)]
    bj = [i for i in bj if 0 < i < len(arr)]

    for i in fi:
        while len(bj) and bj[-1] <= i:
            bj.pop()

        ret += len(bj)

    return ret

input()
print(ans(read_int_list()))
