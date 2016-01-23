#!/usr/bin/env python3

SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

a, b = input().split()
a, b = int(a), int(b)

ret = 0

for i in range(a, b+1):
	s = str(i)
	for c in s:
		ret += SEGMENTS[int(c)]

print(ret)