#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A, B, W):
    W *= 1000
    possible = set()
    for k in range(1, 1100000):
        if A <= W / k <= B:
            possible.add(k)
    if len(possible) == 0:
        return "UNSATISFIABLE"
    return f"{min(possible)} {max(possible)}"

A, B, W = read_int_tuple()
print(ans(A, B, W))