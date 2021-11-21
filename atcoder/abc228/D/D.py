#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

N = 2**20
next_arr = [(i+1) % N for i in range(2**20)]
val_arr = [-1 for i in range(2**20)]

for _ in range(read_int()):
    t, x = read_int_tuple()
    old_x = x
    x %= N
    if t == 2:
        print(val_arr[x])
    elif t == 1:
        while val_arr[x] != -1:
            _x = x
            x = next_arr[x]
            next_arr[_x] = next_arr[next_arr[_x]]
        assert(val_arr[x] == -1)
        val_arr[x] = old_x
