#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A):
    for i in range(1, 3*10**5):
        if i not in A: return i

input()
A = set(read_int_list())
print(ans(A))
