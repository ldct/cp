#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

contests = set()
for _ in range(3):
    contests.add(input())
r = set(["ABC", "ARC", "AGC", "AHC"]) - contests
print(list(r)[0])