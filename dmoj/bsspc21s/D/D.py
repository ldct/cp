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

def make_fill(N, M, val):
    ret = []
    for _ in range(N):
        ret += [[val]*M]
    return ret

N, M, K = read_int_tuple()
if N <= 6e3 and M <= 6e3:
    grid = make_fill(N, M, 0)
    for _ in range(K):
        x, y, X, Y = read_int_tuple()
        x -= 1
        y -= 1
        X -= 1
        Y -= 1
        for i in range(x, X+1):
            for j in range(y, Y+1):
                grid[i][j] = 1

    # print(grid)
    to_check = [(N, M)]

    while True:
        n, m = to_check[-1]
        if n % 2 == 0 and m % 2 == 0:
            to_check += [(n // 2, m // 2)]
        else:
            break

    # print(to_check)

    def check(n, m):
        for i in range(n):
            for j in range(m):
                block = set()
                for x in range(i*(N//n), (i+1)*(N//n)):
                    for y in range(j*(M//m), (j+1)*(M//m)):
                        block.add(grid[x][y])
                if len(block) > 1: return False
        return True

    ret = 0
    for i, (n, m) in enumerate(to_check):
        if check(n, m):
            ret = max(ret, i)

    print(ret)