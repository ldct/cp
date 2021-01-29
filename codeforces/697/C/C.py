#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def ans(pairs):

    deg_a = defaultdict(int)
    deg_b = defaultdict(int)

    for (a, b) in pairs:
        deg_a[a] += 1
        deg_b[b] += 1

    ret = 0

    for (a, b) in pairs:
        rest = len(pairs) - deg_a[a] - deg_b[b] + 1
        ret += rest

    return ret // 2

    return pairs

for _ in range(read_int()):
    a, b, k = read_int_tuple()
    A = read_int_list()
    B = read_int_list()
    print(ans(list(zip(A, B))))