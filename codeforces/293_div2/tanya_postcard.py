#!/usr/bin/env python3

from collections import Counter

def flip_case(c):
	if c in 'abcdefghijklmnopqrstuvwxyz':
		return c.upper()
	else:
		return c.lower()

s_set = Counter(input())
t_set = Counter(input())

yay_count = 0
whoops_count = 0

for s in s_set.keys():
	if s in t_set:
		num_to_remove = min(s_set[s], t_set[s])
		s_set[s] -= num_to_remove
		t_set[s] -= num_to_remove
		yay_count += num_to_remove


for s in s_set.keys():
	S = flip_case(s)
	if S in t_set:
		num_to_remove = min(s_set[s], t_set[S])
		s_set[s] -= num_to_remove
		t_set[S] -= num_to_remove
		whoops_count += num_to_remove

print(yay_count, whoops_count)