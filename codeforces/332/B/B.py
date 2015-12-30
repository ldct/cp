#!/usr/bin/env python3

import sys

n, m = input().split()
n = int(n)
m = int(m)

f = list(map(int, input().split()))
b = list(map(int, input().split()))

i_of_f = {}

amb = False

for j, f_i in enumerate(f):
  i = j+1

  if (f_i in i_of_f):
    amb = True
  else:
    i_of_f[f_i] = i

for i in range(len(b)):
  if (b[i] not in i_of_f):
    print("Impossible")
    sys.exit(0)
  b[i] = i_of_f[b[i]]

if amb:
  print("Ambiguity")
  sys.exit(0)
else:
  print("Possible")
  print(' '.join(str(i) for i in b))