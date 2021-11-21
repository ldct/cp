#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(X, A):
    X -= 1
    A = [a-1 for a in A]
    visited = set()
    while X not in visited:
        visited.add(X)
        X = A[X]
    return len(visited)

    return X, A

N, X = read_int_tuple()
A = read_int_list()
print(ans(X, A))