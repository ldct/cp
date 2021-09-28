#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import bisect

def LIS(arr):
  if len(arr) == 0:
    return 0
  l = [arr[0]]

  for element in arr[1:]:
    pos = bisect.bisect(l, element)
    if pos == len(l):
      if element > l[pos - 1]:
        l.append(element)
    else:
      if element != l[pos - 1]:
        l[pos] = element
  return len(l)

def ans(pairs):
    pairs.sort(key=lambda p: (p[0],-p[1]))
    pairs = [y for x,y in pairs]
    return LIS(pairs)

### CODE HERE

if False:
    print(ans([
        [1,1],
        [1,2],
        [1,3],
    ]))
else:
    N, M = read_int_tuple()

    pairs = []

    for _ in range(M):
        pairs += [read_int_tuple()]

    print(ans(pairs))
