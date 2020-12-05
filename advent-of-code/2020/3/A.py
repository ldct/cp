#!/usr/bin/env pypy3

import sys

lines = []
for line in sys.stdin:
    lines += [line[0:-1]]

def ans(right, down):
    ret = 0
    x, y = 0, 0
    while x < len(lines):
        if lines[x][y] == '#':
            ret += 1

        x += down
        y += right
        y %= len(lines[0])

    return ret

print(ans(1,1) * ans(3, 1) * ans(5, 1) * ans(7, 1) * ans(1, 2))