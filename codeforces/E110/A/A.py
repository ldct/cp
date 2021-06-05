#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def max2(lst):
    return sorted(lst)[::-1][0:2]

def ans(a, b, c, d):
    return 'YES' if (set(max2([a, b, c, d])) == set([max(a, b), max(c, d)])) else 'NO'

for _ in range(read_int()):
    print(ans(*read_int_tuple()))