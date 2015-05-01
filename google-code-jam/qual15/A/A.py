#!/usr/bin/env python3

T = int(input())

for t in range(T):
	l = input().split(' ')[1]
	vals = [int(i) for i in l]

	prefixes = [vals[0]]
	for i in range(1, len(vals)):
		prefixes += [prefixes[i - 1] + vals[i]]

	diffs = [i + 1 - prefixes[i] for i in range(len(prefixes))]
	max_diff = max(diffs)

	ans = max(max_diff, 0)

	print("Case #%d: %d" % (t + 1, ans))