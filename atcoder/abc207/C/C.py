#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

intervals = []

for _ in range(read_int()):
    t, l, r = read_int_tuple()
    if t == 1: intervals += [(l, r)]
    if t == 2: intervals += [(l, r-0.1)]
    if t == 3: intervals += [(l+0.1, r)]
    if t == 4: intervals += [(l+0.1, r-0.1)]

def intersects(a, b):
    (i, j) = a
    (k, l) = b
    if j < k: return False
    if i > l: return False
    return True

ret = 0
for i in range(len(intervals)):
    for j in range(i+1, len(intervals)):
        if intersects(intervals[i], intervals[j]): ret += 1

print(ret)