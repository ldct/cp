#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import heapq

A = [5, 2, 1]

def ans_slow(A):
    A = [-a for a in A]
    heapq.heapify(A)

    last = None
    ret = 0

    while len(A) > 0:
        next = heapq.heappop(A)
        next += 1
        ret += 1

        if last is not None:
            heapq.heappush(A, last)

        last = next
        if last == 0:
            last = None

    return ret

def ans(A):
    A = sorted(A)[::-1]
    ret = sum(A)
    missing = max(A) - sum(A[1:]) - 1
    if missing < 0: missing = 0
    return ret - missing

for _ in range(100):
    import random
    for N in range(1, 10):
        A = [random.randint(1, 100) for _ in range(N)]
    assert(ans_slow(A) == ans(A))
