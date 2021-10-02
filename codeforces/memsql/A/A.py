#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def match(A, B):
    if len(A) != len(B): return False
    for a, b in zip(A, B):
        if a == b or b == "." or a == ".": continue
        return False
    return True

def ans(s):
    choices = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    for c in choices:
        if match(c, s): return c

input()
print(ans(input()))
