#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def small(R, r):
    return R - r

def ans(r1, r2, r3):
    if r3 > r1: return 0

    gap = r2 - r1 - 2*r3

    ret = 0
    ret += (r1-r3)**2

    if gap > 0 and gap > 2*r3:
        ret += (r1 + r3 + gap)**2
        ret -= (r1 + r3)**2

    return ret / ((r2-r3)**2)

for _ in range(read_int()):
    print(ans(*read_int_tuple()))