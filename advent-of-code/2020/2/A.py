#!/usr/bin/env pypy3

import sys

ret = 0
lst = []
for line in sys.stdin:
    [bounds, letter, pwd] = line.split()
    [low, high] = bounds.split('-')
    low = int(low)-1
    high = int(high)-1
    letter = letter[0]

    is_ok = [pwd[low], pwd[high]].count(letter) == 1
    if is_ok:
        ret += 1
print(ret)
