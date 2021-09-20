#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S1 = input()
S2 = input()
S3 = input()
T = input()

ret = ""
for c in T:
    ret += [S1, S2, S3][int(c)-1]

print(ret)