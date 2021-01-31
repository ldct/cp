#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

A, B, C = read_int_tuple()

if A > B:
    print("Takahashi")
elif A < B:
    print("Aoki")
elif C == 0:
    print("Aoki")
else:
    print("Takahashi")