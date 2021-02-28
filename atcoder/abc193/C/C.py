#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    ret = set()
    for b in range(2, N):
        if b*b > N: break
        for e in range(2, 10000000):
            if b**e <= N:
                ret.add(b**e)
            else:
                break
    return N - len(ret)

print(ans(read_int()))