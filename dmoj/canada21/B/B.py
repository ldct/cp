#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def make_kd_tree(points, dim=3, i=0):
    if len(points) > 1:
        points.sort(key=lambda x: x[i])
        i = (i + 1) % dim
        half = len(points) >> 1
        return [
            make_kd_tree(points[: half], dim, i),
            make_kd_tree(points[half + 1:], dim, i),
            points[half]
        ]
    elif len(points) == 1:
        return [None, None, points[0]]

# For the closest neighbor
def get_nearest(kd_node, point, dim, dist_func, return_distances=True, i=0, best=None):
    if kd_node is not None:
        dist = dist_func(point, kd_node[2])
        dx = kd_node[2][i] - point[i]
        if not best:
            best = [dist, kd_node[2]]
        elif dist < best[0]:
            best[0], best[1] = dist, kd_node[2]
        i = (i + 1) % dim
        # Goes into the left branch, and then the right branch if needed
        for b in [dx < 0] + [dx >= 0] * (dx * dx < best[0]):
            get_nearest(kd_node[b], point, dim, dist_func, return_distances, i, best)
    return best if return_distances else best[1]

def dist(p1, p2):
    ret = 0
    for a, b in zip(p1[0:3], p2[0:3]):
        ret += abs(a - b)
    return ret + abs(p1[-1] - p2[-1]) / 100000

points = []
N, Q = read_int_tuple()
for i in range(N):
    (x, y, z) = read_int_tuple()
    points += [(x, y, z, i)]

tree = make_kd_tree(points)

for _ in range(Q):
    (x, y, z) = read_int_tuple()
    q = (x, y, z, 0)
    _, p = get_nearest(tree, q, 3, dist_func=dist)
    print(p[-1]+1)