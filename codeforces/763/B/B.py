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

### CODE HERE

def ans(ranges):

    ans_of = dict()

    for l, r in ranges:
        if l == r:
            ans_of[l] = (l, l)

    for a, b in ranges:
        for l, r in ranges:
            if b == r and a == l+1:
                ans_of[l] = (l, r)
            if a == l and r == b+1:
                ans_of[r] = (l, r)

    leftmost = dict()
    rightmost = dict()

    for l, r in ranges:
        if r not in leftmost: leftmost[r] = l
        leftmost[r] = min(leftmost[r], l)
        if l not in rightmost: rightmost[l] = r
        rightmost[l] = max(rightmost[l], r)

    for x in range(1, N+1):
        if x in ans_of:
            l, r = ans_of[x]
            print(l, r, x)
            continue
        r = x-1
        l = x+1
        if r == 0:
            L = 1
        else:
            L = leftmost[r]
        if l == N+1:
            R = N
        else:
            R = rightmost[l]

        print(L, R, x)

    print()

for _ in range(read_int()):
    N = read_int()
    ranges = []
    for _ in range(N):
        ranges += [read_int_tuple()]
    ans(ranges)