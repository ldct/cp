#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
A = read_int_list()
B = read_int_list()

r = sum(a*b for a,b in zip(A,B))
if r == 0:
    print("Yes")
else:
    print("No")