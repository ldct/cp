#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

for _ in range(T):
    input()
    print(ans(input()))
