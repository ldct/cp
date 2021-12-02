#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A):
    N = len(A)
    minA = min(A)
    ret = []
    for a in A:
        if len(ret) == (N // 2): break
        if a == minA: continue
        ret += [(a, minA)]
    for x, y in ret:
        print(x, y)

for _ in range(read_int()):
    input()
    A = read_int_list()
    ans(A)