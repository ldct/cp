#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()

i = 1
ret = 0

while True:
    if int(str(i) + str(i)) > N:
        break
    i += 1
    ret += 1

print(ret)