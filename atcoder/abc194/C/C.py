#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter, defaultdict

### CODE HERE

input()
A = Counter(read_int_list())
ret = 0
for i in range(-300, 300):
    for j in range(-300, 300):
        ret += A[i]*A[j]*(i - j)**2
print(ret // 2)