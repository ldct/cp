#!/usr/bin/env pypy3

import sys

ret = 0
for line in sys.stdin:
    x = int(line)
    ret += (x // 3) - 2

print(ret)