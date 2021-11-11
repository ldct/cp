#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from math import gcd

### CODE HERE

def multi_gcd(arr):
    ret = arr[0]
    for a in arr:
        ret = gcd(a, ret)
    return ret

def red_length(lst):
    lst = list(lst)
    lst.sort()
    ret = []

    def reducible(x):
        for d in ret:
            if x % d == 0:
                return True
        return False

    for l in lst:
        if not reducible(l):
            ret += [l]
    return len(ret)

def sig(a, b):
    g = gcd(abs(a), abs(b))
    return g, (a // g, b // g)

points = [read_int_tuple() for _ in range(read_int())]

coefficients = defaultdict(set)

for i in range(len(points)):
    for j in range(len(points)):
        if i == j: continue
        x, y = points[i]
        x -= points[j][0]
        y -= points[j][1]

        g, s = sig(x, y)

        coefficients[s].add(g)

ret = 0
for k in coefficients:
    ret += 1

print(ret)