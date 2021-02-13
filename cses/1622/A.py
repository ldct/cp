#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import permutations

S = input()

ret = set()
for p in permutations(S):
    ret.add(''.join(p))

ret = list(sorted(ret))
print(len(ret))
list(map(print, ret))
