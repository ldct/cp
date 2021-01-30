#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import math
from fractions import Fraction

def ans(k, P):
    ret = 0
    a = P[0]
    for i in range(1, len(P)):
        new_a = max(a, math.ceil(Fraction(100*P[i], k)))
        ret += (new_a - a)
        a = new_a + P[i]
    return ret

for _ in range(read_int()):
    n, K = read_int_tuple()
    P = read_int_list()
    print(ans(K, P))