#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from heapq import *

### CODE HERE

walls = []
N, D = read_int_tuple()
for _ in range(N):
    walls += [read_int_tuple()]

walls.sort(lambda p: p[1])

R = -1
ret = 0
for i in range(len(walls)):
    l, r = walls[i]
    if l <= R: continue
    R = r+D-1
    # print(R)
    ret += 1

print(ret)