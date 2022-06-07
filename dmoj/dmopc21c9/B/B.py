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

def expand(x):
    x = ord(x)
    x -= 1
    return [chr(x), chr(x)]

def ans(A, B):
    A = list(A[::-1])
    B = list(B[::-1])

    while True:
        if len(A) == 0 and len(B) == 0: return True
        if len(A) == 0 or len(B) == 0: return False

        if A[-1] == B[-1]:
            A.pop()
            B.pop()
            continue

        if A[-1] > B[-1]: return False

        b = B[-1]
        B.pop()

        lst = expand(b)

        B += lst

    return A, B

for _ in range(read_int()):
    print("YES" if ans(*input().split(" ")) else "NO")