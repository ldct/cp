#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A, B):
    for L in range(len(A), -1, -1):
        for i in range(len(A)):
            if len(A[i:i+L]) != L: continue
            if A[i:i+L] in B:
                return len(A) + len(B) - 2*L

for _ in range(read_int()):
    print(ans(input(), input()))