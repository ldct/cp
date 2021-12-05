#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    if N >= 42: N += 1
    N = str(N)
    while len(N) < 3:
        N = "0" + N
    return f"AGC{N}"

print(ans(read_int()))