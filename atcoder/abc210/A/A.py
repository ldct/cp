#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, A, X, Y = read_int_tuple()

ret = 0
for i in range(1, N+1):
    # print(i, X if i <= A else Y)
    ret += X
    if i > A: ret += (Y-X)

print(ret)