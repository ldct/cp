#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

A, B = input().split()
A = A[::-1]
B = B[::-1]

def ans(A, B):
    for i in range(min(len(A), len(B))):
        if int(A[i]) + int(B[i]) >= 10:
            return "Hard"
    return "Easy"

print(ans(A, B))