#!/usr/bin/env pypy3
import sys

def ans(A, M):
  A = [a % M for a in A]
  def sums(arr):
    if len(arr) <= 1:
      # print(f"sums {arr} = {set(arr)}")
      return set(arr)
    s = len(arr) // 2
    left = arr[0:s]
    right = arr[s:]

    left = sums(left)
    if left == None: return None
    right = sums(right)
    if right == None: return None

    ret = set()
    for a in left:
      for b in right:
        ret.add((a + b) % M)

    if 0 in ret: return None

    ret = ret | left | right

    # print(f"sums {len(arr)} = {len(ret)}")
    return ret

  r = sums(A)
  if r is None: return "YES"
  if 0 in r: return "YES"
  return "NO"

if False:
  import random
  N = 500
  tc = [random.randint(1, 10**6) for _ in range(N)]
  M = 997
  print(ans(tc, M))
else:
  N, M = input().split()
  A = list(map(int, input().split()))
  N = int(N)
  M = int(M)

  print(ans(A, M))