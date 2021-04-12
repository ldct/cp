#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def ans(A):
    freq = defaultdict(int)
    for a in A:
        freq[a] += 1
    spy = None
    for a in A:
        if freq[a] == 1:
            spy = a
    return A.index(spy) + 1

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))