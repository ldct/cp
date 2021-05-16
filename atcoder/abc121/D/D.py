#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def f(x):
    ret = 0
    for i in range(x+1):
        ret ^= i
    return ret

def f_fast(N):
    if N % 4 == 0: return N
    if N % 4 == 1: return 1
    if N % 4 == 2: return N+1
    if N % 4 == 3: return 0

A, B = read_int_tuple()
print(f_fast(B) ^ f_fast(A-1))
