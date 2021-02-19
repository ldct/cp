#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A):
    spare = 0
    for i in range(len(A)):
        spare += A[i] - i
        if spare < 0: return "NO"
    return "YES"

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))