#!/usr/bin/env python3
import sys

N, M = input().split()
A = list(map(int, input().split()))
N = int(N)
M = int(M)

if N > M:
  print('YES')
  sys.exit(0)

sys.setrecursionlimit(2000)

Q_memo = {}

for i, a in enumerate(A):
  A[i] = A[i] % M

def Q(i, K, empty_sequence_ok):
  # true if there exists a subset of (A[0]...A[i]) that sums to K

  # print('Q(%d, %d, %r)' % (i, K, empty_sequence_ok))

  if empty_sequence_ok and K == 0: return True
  if i == 0: return A[0] == K

  args = (i, K, empty_sequence_ok)
  if args not in Q_memo:
    Q_memo[args] = Q(i - 1, K, empty_sequence_ok) or Q(i - 1, (K - A[i]) % M, True)
  return Q_memo[args]

if Q(N-1, 0, False):
  print('YES')
else:
  print('NO')