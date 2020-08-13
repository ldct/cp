#!/usr/bin/env pypy3

n, m, sx, sy = input().split()
n = int(n)
m = int(m)
sx = int(sx)
sy = int(sy)

sx -= 1
sy -= 1

def visit(x, y):
    print(x+1, y+1)

x = sx
y = sy
for _ in range(n):
    for j in range(m):
        visit(x, y)
        y += 1
        y %= m
    y -= 1
    y %= m
    x += 1
    x %= n