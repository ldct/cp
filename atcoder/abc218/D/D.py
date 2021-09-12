#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ok(sp, p, q):
    min_x = min(p[0], q[0])
    max_x = max(p[0], q[0])
    min_y = min(p[1], q[1])
    max_y = max(p[1], q[1])

    if min_x == max_x: return None
    if min_y == max_y: return None

    for x in [min_x, max_x]:
        for y in [min_y, max_y]:
            if (x, y) not in sp: return None

    return (min_x, max_x, min_y, max_y)

def ans(points):
    sp = set(points)
    ret = set()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            r = ok(sp, points[i], points[j])
            if r is not None:
                ret.add(r)
    return len(ret)

points = []
for _ in range(read_int()):
    points += [read_int_tuple()]

print(ans(points))