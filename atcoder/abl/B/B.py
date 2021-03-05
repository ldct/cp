#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def intersects(i, j, k, l):
    if j < k: return False
    if i > l: return False
    return True

A, B, C, D = read_int_tuple()
print("Yes" if intersects(A, B, C, D) else "No")