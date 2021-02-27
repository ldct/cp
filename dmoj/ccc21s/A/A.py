#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
heights = read_int_list()
widths = read_int_tuple()

area = 0

for i in range(len(widths)):
    area += widths[i]*(heights[i] + heights[i+1])

print(area/2)