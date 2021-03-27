#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, M, p):
    p -= 1

    x = p % N
    y = p // N

    return x*M + y + 1

    return x,y

    p += 1
    return X

for _ in range(read_int()):
    N, M, X = read_int_tuple()
    print(ans(N, M, X))