#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from math import gcd

def lcm(a, b):
    return a*b // gcd(a,b)

def _gcd(*args):
    if len(args) == 1:
        return args[0]
    return gcd(*args)

### CODE HERE

N, M = read_int_tuple()

A = [1]*N
requirements = []

for _ in range(M):
    x, y, w = read_int_tuple()
    x -= 1
    requirements += [(x, y, w)]
    for i in range(x, y):
        A[i] = lcm(w, A[i])

def ok():
    for x, y, w in requirements:
        if w != _gcd(*A[x:y]):
            return False
    return True

if ok():
    print(*A)
else:
    print("Impossible")