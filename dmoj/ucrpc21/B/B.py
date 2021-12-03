#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

d = ['x',1,2,3,4,5]

N = read_int()
for _ in range(N):
    i, j = read_int_tuple()
    d[i], d[j] = d[j], d[i]

print(d.index(3))