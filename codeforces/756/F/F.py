#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S, A):
    return S, A

for _ in range(read_int()):
    N, S = read_int_tuple()
    A = read_int_list()
    print(ans(S, A))