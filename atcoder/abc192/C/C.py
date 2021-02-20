#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def f(x):
    s = str(x)
    g1 = sorted(s)
    g2 = g1[::-1]
    return int(''.join(g2)) - int(''.join(g1))

def ans(N, K):
    for _ in range(K):
        N = f(N)
    return N

N, K = read_int_tuple()
print(ans(N, K))