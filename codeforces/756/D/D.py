#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(B, P):
    N = len(P)
    height = [-1]*(N+1)
    for i in range(N):
        height[P[i]] = i
    ret = [0]*(N+1)
    for i in range(N):
        u = i+1
        v = B[i]
        if u == v: continue
        d = height[u] - height[v]
        # print(f"{u} -> {v} ({d})")
        ret[u] = d
    ret = ret[1:]
    if min(ret) < 0: return [-1]
    return ret

for _ in range(read_int()):
    N = read_int()
    B = read_int_list()
    P = read_int_list()
    print(*ans(B, P))