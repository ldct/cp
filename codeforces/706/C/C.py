#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from math import sqrt

### CODE HERE

def ans(points):
    A = []
    B = []

    for x, y in points:
        if x == 0:
            A += [(y)]
        elif y == 0:
            B += [(x)]
        else:
            assert(False)

    A = sorted(A)
    B = sorted(B)

    ret = 0
    for x, y in zip(A, B):
        ret += sqrt(x**2 + y**2)

    return ret


for _ in range(read_int()):
    N = read_int()
    points = []
    for _ in range(2*N):
        x, y = read_int_tuple()
        points += [(abs(x), abs(y))]
    print(ans(points))