#!/usr/bin/env python3

"""
The Just Oishi Ichigo Farm (hereinafter referred to as the JOI Farm) is a strawberry farm that is famous for being long and thin in the east and west, and its entrance is located in the westernmost part of the farm. In the following, the point k meters east of the entrance called point k.

Within the JOI farm there are N strawberries. The are numbered 1 to N. Each strawberry is blue until time 0. Strawberry i bears fruit at point Ai, and at time Ti, the fruit ripens and becomes red.

Strawberries cannot be harvested when they are green. In other words, strawberries cannot be harvested until time Ti. You start at time 0 from the entrance to the plantation at point 0, going east-west at a maximum speed of 1 meter per second. Harvesting strawberries on the move. We assume that the time it takes to harvest a strawberry is negligible.

Given information about strawberry farms, write a program to find the minimum amount of time it takes to return to the entrance after harvesting all the strawberries in red.
"""

N = int(input())

S = []

for _ in range(N):
    a, t = input().split(' ')
    a = int(a)
    t = int(t)
    S += [(a, t)]

S = sorted(S)

max_length = S[-1][0]

# print(S)

S = S[::-1]

for i in range(len(S)):
    (a, t) = S[i]
    S[i] = t - max_length - (max_length - a)

# print(S)

pause_time = max([0] + S)

# print("pause_time=", pause_time)

print(2*max_length + pause_time)
