#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A, B):
    r = 0
    for x in A + B:
        r ^= x
    if sorted(A) == sorted([b ^ r for b in B]):
        return r
    return -1
input()
A = read_int_list()
B = read_int_list()
print(ans(A, B))