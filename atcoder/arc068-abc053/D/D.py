#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter

### CODE HERE

def ans(A):
    ret = len(set(A))
    ntk = []
    for x in list(Counter(A).values()):
        if x > 1:
            ntk += [x - 1]
    return ret - (sum(ntk) % 2)

input()
print(ans(read_int_list()))