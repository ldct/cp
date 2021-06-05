#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import product

def ok(p):
    if p.count('0') != p.count('1'): return False
    num_0 = 0
    num_1 = 0

    for c in p:
        if c == '0': num_0 += 1
        if c == '1': num_1 += 1
        if num_1 > num_0: return False

    return True

N = read_int()

ret = []
for p in product('01', repeat=2*N):
    s = ''.join(p)
    if ok(s): ret += [s]

print(*sorted(ret))