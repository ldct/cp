#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(s):
    s = s[::-1]
    if s[0:2] == "re": return "er"
    return "ist"

### CODE HERE

print(ans(input()))
