#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = input()

curr = 1
ret = 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        curr += 1
    else:
        curr = 1
    ret = max(ret, curr)
print(ret)