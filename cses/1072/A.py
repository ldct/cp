#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(n):
    return (n - 1)*(n + 4)*(n**2 - 3*n + 4)//2
for i in range(read_int()):
    print(ans(i+1))