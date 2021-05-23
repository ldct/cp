#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

input()
A = read_int_list()
B = read_int_list()
C = read_int_list()

index_C = defaultdict(int)
index_B = defaultdict(int)

for i, c in enumerate(C):
    index_C[c] += 1

for i, b in enumerate(B):
    index_B[b] += index_C[i+1]

ret = 0
for a in A:
    ret += index_B[a]

print(ret)
