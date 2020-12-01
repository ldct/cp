#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [int(line)]

for i in range(len(lst)):
    for j in range(i, len(lst)):
        for k in range(j, len(lst)):
            if lst[i] + lst[j] + lst[k] == 2020:
                print(lst[i]*lst[j]*lst[k])
