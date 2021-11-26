#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):
    if int(S[-1]) % 2 == 0: return 0
    if int(S[0]) % 2 == 0: return 1
    for c in S:
        if int(c) % 2 == 0: return 2
    return -1

for _ in range(read_int()):
    print(ans(input()))