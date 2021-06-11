#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S, R = read_int_tuple()
if S*S > 3.14*R*R:
    print("SQUARE")
else:
    print("CIRCLE")