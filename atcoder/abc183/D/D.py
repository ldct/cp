#!/usr/bin/env pypy3

[N, W] = list(map(int, input().split()))

events = []

for _ in range(N):
	[S, T, P] = list(map(int, input().split()))
	events += [(S, P)]
	events += [(T-0.5, -P)]

events = sorted(events)

def ok(events):
	usage = 0
	for _, d in events:
		usage += d
		if usage > W:
			return "No"
	return "Yes"

print(ok(events))