#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

P = read_int()
curr = 15
ret = 0
while P:
    while factorial(curr) > P: curr -= 1
    P -= factorial(curr)
    ret += 1
print(ret)