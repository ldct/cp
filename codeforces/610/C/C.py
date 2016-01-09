#!/usr/bin/env python3
import sys

def flatten(iter_lst):
    return list(item for iter_ in iter_lst for item in iter_)

def repeatPattern(a, b, totalLength):

  totalLength = len(a)*len(b)
  ret = [None]*totalLength
  x = 0
  for i in a:
    for j in b:
      ret[x] = i*j
      x += 1
  return tuple(ret)

def vectors(k):
  if k == 0:
    return set([(1,)])
  if k == 1:
    return set(((1, 1), (1, -1)))
  else:
    vk = vectors(k-1)
    ret = set()
    for a in vectors(1):
      for b in vk:
        ret.add(repeatPattern(a, b, None))
    return ret

def string(v):
  return ''.join("+" if i == 1 else "*" for i in v)

def strings(k):
  return map(string, vectors(k))

N = int(input())
for s in strings(N):
  print(s)
# for _ in range(100):
#   strings(N)
