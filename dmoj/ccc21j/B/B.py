#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

bids = []
for i in range(read_int()):
    name = input()
    bid = read_int()
    bids += [(-bid, i, name)]

_, _, name = min(bids)
print(name)