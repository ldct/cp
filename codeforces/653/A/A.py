#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(x, y, n):
    gap = ((n - y) % x + x) % x
    return n - gap

T = int(input())

for _ in range(T):
    x, y, n = input().split(' ')
    x = int(x)
    y = int(y)
    n = int(n)
    print(ans(x, y, n))
