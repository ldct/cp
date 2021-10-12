#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(x, y):
    x-=1
    y-=1
    ring = max(x,y)
    start = ring**2 + 1

    progress = y + (ring - x)
    if ring % 2 == 1:
        progress = (2*ring) - progress

    return start + progress

for _ in range(read_int()):
    print(ans(*read_int_tuple()))