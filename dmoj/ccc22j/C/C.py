#!/usr/bin/env pypy3

import io, os
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

S = input()
lexed = []

last_str = ""

def is_digit(c):
    return c in "0123456789"

def clear():
    global last_str, lexed
    if len(last_str):
        lexed += [last_str]
    last_str = ""

for c in S:
    if c in "+-":
        clear()
        last_str += c
    elif is_digit(c):
        if len(last_str) and is_digit(last_str[-1]):
            last_str +=c
        else:
            clear()
            last_str += c
    else:
        if len(last_str) and not is_digit(last_str[-1]):
            last_str += c
        else:
            clear()
            last_str += c

clear()

assert(len(lexed) % 3 == 0)
N = len(lexed) // 3
for j in range(N):
    i = 3*j
    # print(i)
    print(lexed[i], "tighten" if lexed[i+1] == "+" else "loosen", lexed[i+2])
