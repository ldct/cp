#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import Counter
from heapq import *

def ans(A):
    freqs = Counter(A)

    worklist = []
    for f in freqs.values():
        worklist += [-f]

    heapify(worklist)

    while len(worklist) >= 2:
        # print(worklist)
        a = heappop(worklist)
        b = heappop(worklist)
        a += 1
        b += 1
        if a != 0:
            heappush(worklist, a)
        if b != 0:
            heappush(worklist, b)

    # print(worklist)

    if len(worklist) == 0: return 0
    return -worklist[0]

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))