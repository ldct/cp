#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

strings = set()
for _ in range(4):
    strings.add(input())
print("Yes" if strings == set(["H", "2B", "3B", "HR"]) else "No")