#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

mountains = []

for _ in range(read_int()):
    name, height = input().split()
    mountains += [(int(height), name)]

mountains = sorted(mountains)[::-1]
print(mountains[1][1])