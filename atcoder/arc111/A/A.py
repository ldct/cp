#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

[N, M] = read_int_list()
d = pow(10, N, M)
rmd = pow(10, N, M*M)
rm = rmd - d

assert(rm % M == 0)
print(rm // M)