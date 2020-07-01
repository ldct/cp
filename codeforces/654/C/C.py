#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(a, b, n, m):
    if m > min(a, b): return "No"
    if n + m > a + b: return "No"
    return "Yes"

T = int(input())

for _ in range(T):
    a, b, n, m = input().split(' ')
    a = int(a)
    b = int(b)
    n = int(n)
    m = int(m)
    print(ans(a, b, n, m))