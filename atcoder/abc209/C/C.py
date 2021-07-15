#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
C = sorted(read_int_list())

ret = 1
sub = 0

for i,c in enumerate(C):
    ret *= c - sub
    sub += 1
    ret %= (10**9+7)

print(ret)