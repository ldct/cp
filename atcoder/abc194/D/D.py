#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter, defaultdict

### CODE HERE

N = read_int()
r = [N/i for i in range(1, N)]
print(sum(r))