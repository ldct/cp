#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import product

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

def max_c(x, base):
    maxes = [cdiv(x, b) for b in base]
    ret = 1
    for r in maxes:
        ret *= r
    return ret

def min_cardinality(base):
    base = list(set(base))
    base.sort()
    A = max(base)+1
    red = 0
    ret = [0]*A
    for b in base:
        if ret[b] == 1:
            red += 1
            continue
        ret[b] = 1
        for i in range(len(ret)):
            if ret[i] == 1:
                if i+b < len(ret):
                    ret[i+b] = 1
    return len(base) - red

if True:
    for _ in range(read_int()):
        input()
        print(min_cardinality(read_int_list()))