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
import random

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def ok_i(j, rockets, distance):
    ret = 0
    for i in range(len(rockets)):
        ret += rockets[i][0]
        if i != j:
            ret -= rockets[i][1]
    return ret >= distance

def ok(rockets, distance):
    for i in range(len(rockets)):
        if ok_i(i, rockets, distance):
            return True
    return False

def ans_slow(rockets, distance):
    ret = float("inf")
    for chosen in subsets(rockets):
        if ok(chosen, distance):
            ret = min(ret, len(chosen))
    return ret

def ans_fast(rockets, distance):
    rockets = sorted(rockets)[::-1]

    head = rockets[0]
    rockets = rockets[1:]
    rockets = [a - b for a, b in rockets]
    rockets = sorted(rockets)[::-1]

    ret = 1
    distance -= head[0]

    if distance <= 0: return 1

    print(head, rockets)

    for i in range(len(rockets)):
        if distance <= 0: return ret

        ret += 1
        distance -= rockets[i]

    if distance <= 0: return ret

    return float("inf")

def mr():
    return (random.randint(1, 5), random.randint(1, 5))

if True:
    tc = [(4, 4), (5, 2)], 7
    print(ans_slow(*tc))
    print(ans_fast(*tc))

elif True:
    for _ in range(1000):
        rockets = [mr() for _ in range(2)]
        dist = random.randint(1, 10)
        if not (ans_fast(rockets, dist) == ans_slow(rockets, dist)):
            print(rockets, dist)
            break
else:
    rockets = [read_int_tuple() for _ in range(read_int())]
    for _ in range(read_int()):
        line = read_int_list()
        if line[0] == 0:
            r = ans_fast(rockets, line[1])
            if r == float("inf"):
                r = -1
            print(r)
        else:
            x = line[1]
            y = line[2]
            rockets[line[0]] = (x, y)
