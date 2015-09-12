#!/usr/bin/env python3

N = input().split()
A = list(map(int, input().split()))

def reduce(N):
  # remove all 2s and 3s in prime factorization of N
  if N % 2 == 0:
    return reduce(N / 2)
  if N % 3 == 0:
    return reduce(N / 3)
  return N

if len(set(reduce(a) for a in A)) == 1:
  print("Yes")
else:
  print("No")