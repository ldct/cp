#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, c):
    if len(set([a, b, c])) == 2:
        common = a+b+c - sum(set([a, b, c]))
        return a+b+c - 2*common
    elif len(set([a, b, c])) == 1:
        return a
    else:
        return 0

a, b, c = read_int_tuple()
print(ans(a, b, c))