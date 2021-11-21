#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S, T, X):
    if T < S: T += 24
    if X < S: X += 24
    X += 0.5
    return S <= X <= T

print("Yes" if ans(*read_int_tuple()) else "No")