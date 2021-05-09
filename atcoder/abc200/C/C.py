#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

read_int()
A = read_int_tuple()
A = [a % 200 for a in A]

freq = defaultdict(int)
for a in A:
    freq[a] += 1

ret = 0
for i in range(200):
    f = freq[i]
    ret += (f*(f-1))//2

print(ret)
