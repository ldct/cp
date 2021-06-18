#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = input()
a = len(S)
z = -1
for i in range(len(S)):
    if S[i] == 'A': a = min(a, i)
    if S[i] == 'Z': z = max(z, i)

print(z-a+1)