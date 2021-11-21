#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(K, P):
    sp = sorted(P)[::-1]
    for p in P:
        print("Yes" if p + 300 >= sp[K-1] else "No")

N, K = read_int_tuple()
P = []
for _ in range(N):
    P += [sum(read_int_list())]
ans(K, P)