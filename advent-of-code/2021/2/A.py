#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [line.replace('\n', '')]

x, y = 0, 0
for line in lst:
    dir, dist = line.split(' ')
    if dir == 'forward':
        x += int(dist)
    elif dir == 'down':
        y += int(dist)
    elif dir == 'up':
        y -= int(dist)
    else:
        assert(False)

print(x*y)
