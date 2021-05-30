#!/usr/bin/env pypy3

import sys
from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def without(points, exclude):
    ret = []
    for i in range(len(points)):
        if i in exclude: continue
        ret += [points[i]]
    return ret

def opp(points, c, e):
    ret = []
    for i in range(len(points)):
        if i in [c, e]: continue
        ret += [dist(points[c], points[i])]
    return ret

def best(points):
    points = sorted(points)
    points = [i for (_, i) in points]

    ret = []

    if len(points) > 0: ret += [points[0]]
    if len(points) > 1: ret += [points[-1]]

    return ret

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    ret = max(abs(x1-x2), abs(y1-y2))
    return ret

def furthest_pair_ij(points):
    p1 = []
    p2 = []
    indices = []

    for i, (x, y) in enumerate(points):
        p1 += [(x, i)]
        p2 += [(y, i)]

    indices += best(p1)
    indices += best(p2)

    indices = set(indices)

    distances = []
    for i in indices:
        for j in indices:
            distances += [(dist(points[i], points[j]), i, j)]

    (d, i, j) = max(distances)

    return d, i, j

def ans(points):

    d, i, j = furthest_pair_ij(points)
    # print(d, i, j)
    if d == 0: return 0

    r2 = []
    r2 += opp(points, i, j)
    r2 += opp(points, j, i)

    # print(sorted(r2))
    points2 = without(points, [i, j])

    # print(points2)
    d, _, _ = furthest_pair_ij(points2)

    r2 += [d]
    return max(r2)

def ans_slow(points):
    dists = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dists += [dist(points[i], points[j])]
    return sorted(dists)[-2]

if False:
    tc = [(1, 3), (0, 1), (1, 0), (2, 1)]
    # print(ans_slow(tc))
    # print(ans(tc))
elif False:
    import random
    for _ in range(10000):
        tc = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(5)]
        assert(ans(tc) == ans_slow(tc))
        if (ans(tc) != ans_slow(tc)):
            assert(False)
            print(tc)
else:
    points = []
    for i in range(read_int()):
        x, y = read_int_tuple()
        points += [(x, y)]

    print(ans(points))
