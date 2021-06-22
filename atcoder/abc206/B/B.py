#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    r = 0
    for i in range(1, N+100):
        r += i
        if r >= N: return i

N = read_int()
print(ans(N))
