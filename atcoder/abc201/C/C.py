#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import product

### CODE HERE

contains = set()
excludes = set()

for i, c in enumerate(input()):
    if c == 'o':
        contains.add(str(i))
    elif c == 'x':
        excludes.add(str(i))

def ok(pin, contains, excludes):
    for c in contains:
        if c not in pin:
            return False
    for e in excludes:
        if e in pin: return False
    return True

if False:
    print(contains, excludes, ok('9999', contains, excludes))
else:
    ret = 0

    for pin in product('0123456789', repeat=4):
        if ok(pin, contains, excludes):
            ret += 1

    print(ret)