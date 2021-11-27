#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import random

print(1)
N = 10**5
print(N)
tc = [random.randint(1,100) for _ in range(N)]
tc.sort()
print(*tc)