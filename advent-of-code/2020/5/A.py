#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [line[:-1]]

lst = [int(line.replace("B", "1").replace("F", "0").replace("L", "0").replace("R", "1"),2) for line in lst]

seats = set(lst)
seats = sorted(seats)

for i in range(0, 1000):
    if i not in seats and (i+1) in seats and (i-1) in seats:
        print(i)
