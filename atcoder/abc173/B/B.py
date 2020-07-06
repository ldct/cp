#!/usr/bin/env python3

from collections import defaultdict

scores = defaultdict(int)

N = int(input())
for _ in range(N):
    S = input()
    assert(S in ['AC', 'WA', 'TLE', 'RE'])
    scores[S] += 1

print(f"AC x {scores['AC']}")
print(f"WA x {scores['WA']}")
print(f"TLE x {scores['TLE']}")
print(f"RE x {scores['RE']}")