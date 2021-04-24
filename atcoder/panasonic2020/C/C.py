#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, c):
    RHS = c - a - b
    return RHS > 0 and 4*a*b < RHS**2

a, b, c = read_int_tuple()
print("Yes" if ans(a, b, c) else "No")