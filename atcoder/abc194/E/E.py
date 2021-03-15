#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

N, M = read_int_tuple()
A = read_int_list()

indexes = defaultdict(list)

for i, e in enumerate(A):
    indexes[e] += [i]

def ans(indexes):
    for i in range(2*10**6):
        lst = indexes[i]
        if len(lst) == 0:
            return i
        lst = [-1] + sorted(lst) + [len(A)]

        for j in range(len(lst)-1):
            if lst[j+1] - lst[j] > M:
                return i

print(ans(indexes))
