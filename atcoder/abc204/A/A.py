#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

x, y = read_int_tuple()

if x == y:
    print(x)
else:
    [z] = set([0,1,2]) - set([x, y])
    print(z)