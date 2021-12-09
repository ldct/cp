#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations
from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

deg = defaultdict(int)

for _ in range(read_int()-1):
    u, v = read_int_tuple()
    deg[u] += 1
    deg[v] += 1

def is_star(deg):
    deg = list(deg.values())
    deg.sort()
    return deg[-2] == 1

if is_star(deg):
    print("Yes")
else:
    print("No")