#!/usr/bin/env pypy3

from functools import reduce

def split(iterable, where):
    def splitter(acc, item, where=where):
        if item == where:
            acc.append([])
        else:
            acc[-1].append(item)
        return acc
    return reduce(splitter, iterable, [[]])

import sys

lst = []
for line in sys.stdin:
    lst += [line[:-1]]

ret = 0
for group in split(lst, ''):
    g = list(map(set, group))
    r = g[0]
    for gg in g[1:]:
        r &= gg
    ret += len(r)

print(ret)