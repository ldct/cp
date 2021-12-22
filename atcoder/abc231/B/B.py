#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left


def argmax(d):
    for ret in d: break
    for k in d:
        if d[k] > d[ret]:  ret = k
    return ret

### CODE HERE

votes = [input() for _ in range(read_int())]
print(argmax(Counter(votes)))