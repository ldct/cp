#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def width(arr):
    if len(arr) % 2 == 1: return 1
    arr = sorted(arr)
    i = len(arr) // 2
    return arr[i] - arr[i-1] + 1

def ans(houses):
    xs = []
    ys = []
    for x, y in houses:
        xs += [x]
        ys += [y]

    return width(xs)*width(ys)

for _ in range(read_int()):
    houses = []
    for _ in range(read_int()):
        houses += [read_int_tuple()]

    print(ans(houses))