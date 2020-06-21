#!/usr/bin/env pypy3

from collections import defaultdict

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

def ans(points, c):
    lines = dict()

    for x, y in points:
        line = y-x
        if line not in lines: lines[line] = []
        lines[line] += [(x, y)]

    checkpoints = 0
    moves = 0

    for points in lines.values():
        occupied = defaultdict(list)
        for x, y in points:
            key = x%c
            occupied[key] += [x]
        checkpoints += len(occupied)

        # print(occupied)

        for xs in occupied.values():
            ss = sorted(xs)
            mid = ss[len(ss) // 2]

            for x in ss:
                assert(abs(mid - x) % c == 0)
                moves += (abs(mid - x) // c)

    print(checkpoints, moves)


for _ in range(T):
    [N, c, *rest] = input().split(' ')
    N = int(N)
    c = int(c)

    points = []

    for _ in range(N):
        [x, y, *rest] = input().split(' ')
        x = int(x)
        y = int(y)

        points += [(x, y)]

    ans(points, c)