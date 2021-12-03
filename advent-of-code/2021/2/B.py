#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [line.replace('\n', '')]

x, y, aim = 0, 0, 0
for line in lst:
    dir, dist = line.split(' ')
    dist = int(dist)
    if dir == 'forward':
        x += dist
        y += aim*dist
    elif dir == 'down':
        aim += int(dist)
    elif dir == 'up':
        aim -= int(dist)
    else:
        assert(False)

print(x*y)
