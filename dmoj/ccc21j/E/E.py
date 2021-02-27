#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

M = read_int()
N = read_int()

nf_row = defaultdict(int)
nf_col = defaultdict(int)

for _ in range(read_int()):
    t, idx = input().split()
    idx = int(idx)-1

    if t == 'R': nf_row[idx] += 1
    if t == 'C': nf_col[idx] += 1

ret = 0

for i in range(M):
    for j in range(N):
        if (nf_row[i] + nf_col[j]) % 2 == 1:
            ret += 1

print(ret)
