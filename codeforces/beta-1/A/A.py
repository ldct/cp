#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

### CODE HERE

N, M, A = read_int_tuple()
print(cdiv(N, A) * cdiv(M, A))