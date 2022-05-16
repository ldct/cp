#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

from math import sqrt

def draw_circle_filled_wrong(R):
    grid = []
    for _ in range(R+1):
        grid += [[" "]*(R+1)]

    def draw_circle_perimeter(R):
        for x in range(0, R+1):
            y = round(sqrt(R * R - x * x))
            grid[x][y] = "█"
            grid[y][x] = "█"

    for r in range(R+1):
        draw_circle_perimeter(r)
    return grid

def draw_circle_filled(R):
    grid = []
    for _ in range(R+1):
        grid += [[" "]*(R+1)]

    for x in range(R+1):
        for y in range(R+1):
            if round(sqrt(x*x + y*y)) <= R:
                grid[x][y] = "█"

    return grid

def ans(N):
    grid0 = draw_circle_filled(N)
    grid1 = draw_circle_filled_wrong(N)

    ret = []
    for x in range(N+1):
        for y in range(N+1):
            if grid0[x][y] > grid1[x][y]:
                if x <= y:
                    ret += [(x, y)]

    return ret

c = defaultdict(int)
for a, b in ans(100):
    c[a] += 1

print(c)
print([c[i] for i in range(1, 50)])

# T = int(input())
# for t in range(T):
#     print("Case #" + str(t+1) + ": " + str(ans(*read_int_tuple())))
