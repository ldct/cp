#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, K, A, edges):
    r = 0
    for a in A: r ^= a
    return r

for _ in range(read_int()):
    N, K = read_int_tuple()
    A = read_int_list()
    edges = []
    for _ in range(N-1):
        edges += [read_int_tuple()]
    print(ans(N, K, A, edges))