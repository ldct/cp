#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def intersect(r1, r2):
    a = max(r1[0], r2[0])
    b = min(r1[1], r2[1])
    if a <= b: return b - a + 1
    return 0

def match(i, N):
    r1 = (1<<i, (1<<(i+1))-1)
    r2 = (1, N)
    r = intersect(r1, r2)
    return r

def ans(N):
    ret = 0
    for i in range(64):
        ret = max(ret, match(i, N))
    return ret

for _ in range(read_int()):
    print(ans(read_int()))
