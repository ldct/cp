#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(shops):
    candidates = [p for a, p, x in shops if x > a]
    if len(candidates) == 0:
        return -1
    return min(candidates)

shops = []
for _ in range(read_int()):
    shops += [read_int_tuple()]

print(ans(shops))