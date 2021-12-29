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

def ans(n, m, x, y, t_x, t_y):
    x -= 1
    y -= 1
    t_x -= 1
    t_y -= 1

    dx = 1
    dy = 1

    for i in range(200):
        # print(x, y)
        if x == t_x or y == t_y: return i

        if (x == 0 and dx == -1): dx = 1
        if (x == n-1 and dx == 1): dx = -1
        if (y == 0 and dy == -1): dy = 1
        if (y == m-1 and dy == 1): dy = -1

        x += dx
        y += dy


    return n, m, x, y, t_x, t_y

for _ in range(read_int()):
    print(ans(*read_int_list()))