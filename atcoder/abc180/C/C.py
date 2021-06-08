#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N):
    ret = set()
    for i in range(1, N+100):
        if i*i > N: break
        if N % i == 0:
            ret.add(i)
            ret.add(N // i)

    return sorted(ret)

for a in ans(read_int()):
    print(a)
