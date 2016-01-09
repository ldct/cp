#!/usr/bin/env python3
import sys

N, M = input().split(' ')
N = int(N)
M = int(M)

turnedOn = set()

for i in range(N):
  bulbs = list(map(int, input().split(' ')))[1:]
  for bulb in bulbs:
    turnedOn.add(bulb)

for i in range(1, M+1):
  if i not in turnedOn:
    print("NO")
    sys.exit(0)

print("YES")
