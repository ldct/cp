#!/usr/bin/env python3
import sys

N, M, Q = input().split()
N = int(N)
M = int(M)
Q = int(Q)

rows = []
score_of_row = []

def score(row):
  score_so_far = 0
  max_score = float('-inf')

  for r in row:
    if r == 0:
      score_so_far = 0
    else:
      score_so_far += 1
    max_score = max(max_score, score_so_far)

  return max_score


for _ in range(N):
  row = [int(x) for x in input().split()]
  rows += [row]
  score_of_row += [score(row)]

for _ in range(Q):
  r, c = input().split()
  r, c = int(r), int(c)

  rows[r-1][c-1] = 1 - rows[r-1][c-1]
  score_of_row[r-1] = score(rows[r-1])

  print(max(score_of_row))