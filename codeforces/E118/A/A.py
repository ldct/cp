#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(t1, p1, t2, p2):
    p = min(p1, p2)
    p1 -= p
    p2 -= p
    if p1 > 15: return '>'
    if p2 > 15: return '<'
    t1*= 10**p1
    t2*= 10**p2
    if t1 > t2: return '>'
    if t1 < t2: return '<'
    return '='

for _ in range(read_int()):
    t1, p1 = read_int_tuple()
    t2, p2 = read_int_tuple()
    print(ans(t1, p1, t2, p2))