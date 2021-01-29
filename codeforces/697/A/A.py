#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(n):
    while n % 2 == 0: n //= 2
    if n == 1: return "NO"
    return "YES"

for _ in range(read_int()):
    print(ans(read_int()))