#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(items):
    L, R = items[0]
    for a, b in items:
        L = max(L, a)
        R = min(R, b)
    if L > R: return 0
    return R-L+1

input()
A = read_int_list()
B = read_int_list()
print(ans(list(zip(A, B))))