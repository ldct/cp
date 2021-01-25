#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

n = read_int()
ret = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    ret += [n]
print(*ret)