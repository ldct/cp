#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def sum(n):
    return n*(n+1)//2

def ans(n, r):
    if r < n:
        return sum(r)
    return sum(n-1) + 1

T = int(input())

for _ in range(T):
    n, r = input().split(' ')
    n = int(n)
    r = int(r)
    print(ans(n, r))