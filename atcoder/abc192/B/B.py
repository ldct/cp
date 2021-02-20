#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = input()
odds = []
evens = []
for i in range(len(S)):
    if i % 2 == 0:
        odds += [S[i]]
    else:
        evens += [S[i]]

def ans(odds, evens):
    for c in odds:
        if not ('a' <= c <= 'z'): return 'No'
    for c in evens:
        if not ('A' <= c <= 'Z'): return 'No'
    return 'Yes'

print(ans(odds, evens))