#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

B = read_int()
P = 5*B - 400
print(P)
if P == 100:
    print(0)
elif P > 100:
    print(-1)
else:
    print(1)