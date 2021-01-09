#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def line_eqn(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    a = y2 - y1
    b = x1 - x2
    c = a*x1 + b*y1

    return (a, b, c)

[sx, sy, gx, gy] = read_int_list()

sy = -sy

a, b, c = line_eqn((sx, sy), (gx, gy))
print(c / a)