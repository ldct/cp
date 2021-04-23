#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import math
from decimal import *

def ans(R, X, Y):
    getcontext().prec = 100
    D = Decimal(X*X + Y*Y).sqrt()
    if R > D: return 2
    return math.ceil(D / R)

def ans_float(R, X, Y):
    D = math.sqrt(X*X + Y*Y)
    return math.ceil(D / R)

print(ans(*read_int_tuple()))
