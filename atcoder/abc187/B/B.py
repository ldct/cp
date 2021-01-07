#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def read_line():
	return list(map(int, input().split()))

def read_int():
	return int(input())

### CODE HERE

points = []

for _ in range(read_int()):
    points += [tuple(read_line())]

ret = 0

def ok(a, b):
    (ax, ay) = a
    (bx, by) = b

    rise = ay - by
    run = ax - bx

    if run == 0: return False
    return abs(rise) <= abs(run)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        if ok(points[i], points[j]):
            ret += 1

print(ret)