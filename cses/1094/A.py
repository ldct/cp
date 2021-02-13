#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
A = read_int_list()

ret = 0

last = A[0]

for a in A[1:]:
    new_a = max(a, last)
    ret += new_a - a
    last = new_a

print(ret)