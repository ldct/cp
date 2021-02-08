#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

V, T, S, D = read_int_tuple()
T *= V
S *= V

if T <= D <= S:
    print("No")
else:
    print("Yes")