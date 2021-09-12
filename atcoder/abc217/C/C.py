#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
P = read_int_list()
P = [(a, i) for i,a in enumerate(P)]
P.sort()
print(*[i+1 for a, i in P])