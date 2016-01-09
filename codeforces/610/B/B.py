#!/usr/bin/env python3
import sys

N = int(input())
colors = list(map(int, input().split()))

minimumColor = min(colors)

a = None
b = None

gaps = set()

for i, e in enumerate(colors):
  if e != minimumColor: continue

  if a == None:
    a = i
    leftMostMin = i
  else:
    b = a
    a = i

    gaps.add(a-b-1)

gaps.add(N - (a - leftMostMin) - 1)

print(N * minimumColor + max(gaps))