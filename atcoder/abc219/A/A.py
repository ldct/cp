#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

X = read_int()

if X >= 90:
    print("expert")
elif X >= 70:
    print(90-X)
elif X >= 40:
    print(70-X)
else:
    print(40-X)