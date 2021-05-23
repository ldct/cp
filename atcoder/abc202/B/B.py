#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = input()
ret = []

for c in S:
    if c == '6':
        ret += ['9']
    elif c == '9':
        ret += ['6']
    else:
        ret += [c]

print(''.join(ret[::-1]))