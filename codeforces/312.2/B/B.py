#!/usr/bin/env python3

import sys

N = int(input())
A = list(map(int, input().split(' ')))

left_idx = {}
right_idx = {}
count = {}

for i, e in enumerate(A):
    if e not in count:
        count[e] = 0
    count[e] += 1
    if e not in left_idx:
        left_idx[e] = i
    if i < left_idx[e]:
        left_idx[e] = i
    if e not in right_idx:
        right_idx[e] = i
    if right_idx[e] < i:
        right_idx[e] = i

max_count = max(count[c] for c in count)
items_with_mc = [i for i in count if count[i] == max_count]

span_i = [(right_idx[i] - left_idx[i], i) for i in items_with_mc]

iwms = min(span_i)[1]

print(left_idx[iwms] + 1, right_idx[iwms] + 1)