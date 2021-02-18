#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, c):
    a, b, c = tuple(sorted([a, b, c]))

    if c**2 == a**2 + b**2: return 'R'
    if c**2 > a**2 + b**2: return 'O'
    return 'A'

for _ in range(read_int()):
    print(ans(*read_int_tuple()))