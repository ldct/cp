#!/usr/bin/env python3

x1, y1 = input().split()
x2, y2 = input().split()

x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

dx = abs(x1-x2)
dy = abs(y1-y2)

print(max(dx, dy))