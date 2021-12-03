#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [int(line)]

ret = 0
for i in range(len(lst)-1):
    if lst[i+1] > lst[i]: ret += 1
print(ret)
