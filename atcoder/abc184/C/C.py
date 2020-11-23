#!/usr/bin/env python3

def ans(l):
    a, b, c, d = l

    if (a, b) == (c, d): return 0

    if a + b == c + d: return 1
    if a - b == c - d: return 1
    if abs(a - c) + abs(b - d) <= 3: return 1

    dx = c - a
    dy = d - b

    dx %= 2
    dx += 2
    dx %= 2

    dy %= 2
    dy += 2
    dy %= 2

    if abs(a + b - c - d) <= 3: return 2
    if abs(a - b - c + d) <= 3: return 2

    if dx == dy: return 2

    return 3

x, y = input().split()
xt, yt = input().split()

print(ans(list(map(int, [x,y,xt,yt]))))