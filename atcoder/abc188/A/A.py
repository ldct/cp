#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

[x, y] = read_int_tuple()
x, y = min(x,y), max(x,y)
if x+3 > y:
    print("Yes")
else:
    print("No")