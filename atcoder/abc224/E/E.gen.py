#!/usr/bin/env pypy3

import random

H = 10**5
W = 10**5
N = 2*10**5
print(H, W, N)
occupied_points = set()
while True:
    if len(occupied_points) == N: break
    x = random.randint(1, H)
    y = random.randint(1, W)
    a = random.randint(1, 10)
    if (x, y) not in occupied_points:
        occupied_points.add((x, y))
        print(x, y, a)