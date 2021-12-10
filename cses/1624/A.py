#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

restrictions = [input() for _ in range(8)]
# print(restrictions)

queens = []
ret = 0

def attacks(a, b, c, d):
    return abs(a - c) == abs(b - d)

def attacks_any(queens, y):
    X = len(queens)
    for x in range(X):
        if attacks(x, queens[x], X, y): return True
    return False

def place():
    global ret, queens
    if len(queens) == 8:
        ret += 1
        return
    for y in range(8):
        if y in queens: continue
        if attacks_any(queens, y): continue
        if restrictions[len(queens)][y] == '*': continue
        queens += [y]
        place()
        queens.pop()

place()
print(ret)
