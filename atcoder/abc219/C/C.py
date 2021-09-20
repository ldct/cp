#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

order = input()
names = []
for _ in range(read_int()):
    names += [input()]

names = [([order.index(c) for c in name], name) for name in names]
names.sort()

for _, name in names:
    print(name)
