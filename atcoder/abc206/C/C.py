#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()
A = read_int_list()

ret = N*(N-1)//2

from collections import defaultdict

f = defaultdict(int)

for a in A:
    f[a] += 1

for k in f:
    v = f[k]
    ret -= v*(v-1)//2

print(ret)
