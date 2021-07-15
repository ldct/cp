#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, X = read_int_tuple()
A = read_int_list()

for i, a in enumerate(A):
    X -= (a - i%2)

print("Yes" if X >= 0 else "No")