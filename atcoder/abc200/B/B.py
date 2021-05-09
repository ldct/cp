#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, K = read_int_tuple()
for _ in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = int(str(N)+"200")
print(N)