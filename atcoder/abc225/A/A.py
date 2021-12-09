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

S = input()
ret = set()
for s in permutations(S):
    ret.add(''.join(s))
print(len(ret))