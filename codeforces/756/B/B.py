#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import operator as op
from functools import reduce

def ans_slow(a, b):
    if b > a: return ans(b, a)
    ret = 0
    while 0 < b < a:
        b -= 1
        a -= 3
        ret += 1
    ret += min(a, b) // 2
    return ret

def ans(a, b):
    if b > a: return ans(b, a)
    trf = min((a - b) // 2, b)
    a -= trf
    b += trf
    return min(a, b) // 2

for _ in range(read_int()):
    print(ans(*read_int_tuple()))