#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

sum = []
dif = []

N = int(input())
for _ in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)

    sum += [x+y]
    dif += [x-y]

ans1 = max(sum) - min(sum)
ans2 = max(dif) - min(dif)

print(max(ans1, ans2))