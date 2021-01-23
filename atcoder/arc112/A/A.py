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

max_a = -1
max_b = -1
ret = -1
for i in range(len(A)):
    max_a = max(max_a, A[i])
    max_b = max(max_b, B[i])
    ret = max(ret, B[i]*max_a)
    print(ret)
