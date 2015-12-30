#!/usr/bin/env python3

from collections import Counter

n = int(input())
h_u = tuple(map(int, input().split()))
h_s = sorted(h_u)

i = 0
a = Counter()
b = Counter()

num_partitions = 0

for i in range(n):
  a[h_u[i]] += 1
  b[h_s[i]] += 1

  if (a == b):
    num_partitions += 1
    a = Counter()
    b = Counter()

print(num_partitions)