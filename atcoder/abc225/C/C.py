#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations
from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

N, M = read_int_tuple()
B = [read_int_list() for _ in range(N)]

def is_cal(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] -= 1
    for row in B:
        for i in range(len(row)-1):
            if row[i+1] - row[i] != 1: return "No"
    for i in range(len(B)-1):
        if B[i+1][0] - B[i][0] != 7: return "No"
    row = B[0]
    start = row[0] % 7
    end = start + len(row) - 1
    # print(start, end)
    if end > 6: return "No"
    return "Yes"

print(is_cal(B))
