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

MAX_DIGITS = 10

def count(x):

    ret = 0

    x = list(map(int, str(x)))
    while len(x) != MAX_DIGITS:
        x = [0] + x

    for i in range(len(x)):
        for j in range(x[i]):
            r = 0

            d = len(x)-i-1

            avg = sum(x[0:i] + [j]) + 4.5*d

            r = sum(x[0:i] + [j])*10**d + 9*d*(10**d)//2

            ret += r
    return ret

def count_slow(n):
    ret = 0
    for x in range(n):
        for c in str(x):
            ret += int(c)
    return ret

def ans(a, b):
    return count(b+1) - count(a)
    return a, b

while True:
    a, b = read_int_tuple()
    if (a, b) == (-1, -1):
        break
    print(ans(a, b))