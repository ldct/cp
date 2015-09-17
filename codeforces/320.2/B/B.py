#!/usr/bin/env python3
import sys

N = int(input())

score_pairings = []
partner_of = {}
people_with_partners = set()

for k in range(2*N - 1):
  i = k + 2
  line = list(map(int, input().split()))
  for j in range(1, i):
    score_pairings += [(line[j-1], (i, j))]

score_pairings = sorted(score_pairings)[::-1]

for score, (i, j) in score_pairings:
  if i in people_with_partners or j in people_with_partners:
    continue
  partner_of[i] = j
  partner_of[j] = i
  people_with_partners.add(i)
  people_with_partners.add(j)

print(' '.join(str(partner_of[i]) for i in partner_of))