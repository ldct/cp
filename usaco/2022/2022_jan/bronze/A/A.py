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

from functools import reduce

### CODE HERE

def f(s):
    return [ord(c) - ord('A') for c in s]

correct = [f(input()) for _ in range(3)]
guess = [f(input()) for _ in range(3)]

found = reduce(list.__add__, correct)

green = [0]*26
yellow = [0]*26

for i in range(3):
    for j in range(3):
        if guess[i][j] == correct[i][j]:
            green[guess[i][j]] += 1

for i in range(3):
    for j in range(3):
        if guess[i][j] in found:
            yellow[guess[i][j]] += 1

yellow2 = []
for i in range(26):
    yellow2 += [min(
        found.count(i) - green[i],
        yellow[i] - green[i]
    )]

print(sum(green))
print(sum(yellow2))