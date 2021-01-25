#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

ops = []

for _ in range(read_int()):
    ops += [input()]

ops = ops[::-1]

def ans(i):
    if i == len(ops):
        return 1
    if ops[i] == 'AND':
        return ans(i+1)
    elif ops[i] == 'OR':
        rest = len(ops) - i
        return 2**rest + ans(i+1)

print(ans(0))