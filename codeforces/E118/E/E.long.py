#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import deque

### CODE HERE

import random

def make_fill(N, M):
    ret = []
    for _ in range(N):
        row = []
        for _ in range(M):
            row += [random.choice('.')]
        ret += [row]
    return ret

print(1)
N = 1
M = 10**6
print(N, M)
tc = make_fill(N, M)
tc[0][0] = 'L'
for row in tc:
    print(''.join(row))