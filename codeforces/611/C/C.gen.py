#!/usr/bin/env python3

N = 500
Q = 100000

from random import randint

print("{0} {0}".format(N))

for i in range(N):
  for j in range(N):
    print(".", end="")
  print()

print("{0}".format(Q))
for _ in range(Q):
  print("1 1 {0} {1}".format(randint(1, N), randint(1, N)))