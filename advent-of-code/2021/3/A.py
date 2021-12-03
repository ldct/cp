#!/usr/bin/env pypy3

import sys

lst = []
for line in sys.stdin:
    lst += [line.replace('\n', '')]

def majority(arr):
    if arr.count('0') > arr.count('1'): return 0
    return 1

lst = list(zip(*lst))
gamma = list(map(majority, lst))[::-1]
eps = [1-x for x in gamma]

gamma = sum([2**i * e for i,e in enumerate(gamma)])
eps = sum([2**i * e for i,e in enumerate(eps)])

print(gamma*eps)
