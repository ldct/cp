#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

lst = read_int_list()
[a, b, c] = list(sorted(lst))
if c - b == b - a:
    print("Yes")
else:
    print("No")