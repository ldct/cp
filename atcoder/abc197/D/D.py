#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from math import cos, sin, pi

N = read_int()
x0, y0 = read_int_tuple()
x_opp, y_opp = read_int_tuple()

x_c = (x0 + x_opp) / 2
y_c = (y0 + y_opp) / 2

t = 2*pi / N

x0 -= x_c
y0 -= y_c

x0, y0 = cos(t)*x0 - sin(t)*y0, sin(t)*x0 + cos(t)*y0

x0 += x_c
y0 += y_c

print(x0, y0)
