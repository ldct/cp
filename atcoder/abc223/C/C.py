#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from fractions import Fraction

### CODE HERE

fuses = []

for _ in range(read_int()):
    fuses += [read_int_tuple()]

total_time = 0
for a, b in fuses:
    total_time += a / b

time = total_time / 2

dist = 0
for a, b in fuses:
    fuse_time = a / b
    if time > fuse_time:
        time -= fuse_time
        dist += a
    else:
        dist += b*time
        break

print(dist)
