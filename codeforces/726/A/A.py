#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans_slow(A):
    a = sum(A)
    b = len(A)
def ans(A):
    a = sum(A)
    b = len(A)
    if a == b: return 0
    if a < 0: return 1
    if a < b: return 1
    return a-b

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))