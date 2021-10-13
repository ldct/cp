#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b):
    p, q = 2*a - b, 2*b - a
    if p % 3 != 0: return "NO"
    if q % 3 != 0: return "NO"
    if p < 0: return "NO"
    if q < 0: return "NO"
    return "YES"

for _ in range(read_int()):
    print(ans(*read_int_list()))