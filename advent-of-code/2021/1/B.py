#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [int(line)]

def window(lst):
    ret = []
    for i in range(len(lst)):
        grp = lst[i:i+3]
        if len(grp) == 3:
            ret += [sum(grp)]
    return ret

def num_increasing(lst):
    ret = 0
    for i in range(len(lst)-1):
        if lst[i+1] > lst[i]: ret += 1
    return ret

print(num_increasing(window(lst)))