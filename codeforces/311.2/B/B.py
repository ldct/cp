#!/usr/bin/env python3

N, W = tuple(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

A.sort()

smallest_girl = A[0]
smallest_boy = A[N]

smallest_girl = min(smallest_girl, smallest_boy / 2)
smallest_boy = min(smallest_boy, smallest_girl * 2)

max_pour = (smallest_boy + smallest_girl) * N

print(min(W, max_pour))