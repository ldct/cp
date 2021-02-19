#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

A = [read_int_list(), read_int_list(), read_int_list()]

marked = set()
for _ in range(read_int()):
    marked.add(read_int())

A = [[a in marked for a in row] for row in A]

def ans(A):
    for row in A:
        if all(row): return "Yes"
    A = list(zip(*A))
    for row in A:
        if all(row): return "Yes"
    if A[0][0] and A[1][1] and A[2][2]: return "Yes"
    if A[0][2] and A[1][1] and A[2][0]: return "Yes"
    return "No"

print(ans(A))