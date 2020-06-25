#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
A = [(a, True) for a in A]

happiness = 0
uses_left = N

while True:
	last_a = None
	for i in range(len(A)):
		a, usable = A[i]
		if not usable: continue
		if last_a is None:
			last_a = a
			A[i] = (a, False)
			uses_left -= 1
			continue
		if last_a < a:
			happiness += 1
			A[i] = (a, False)
			uses_left -= 1
			last_a = a
			continue
	if uses_left == 0: break

print(happiness)