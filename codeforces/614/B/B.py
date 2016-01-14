#!/usr/bin/env python3
import sys

input()
arr = list(input().split())

ans = 1
for s in arr:
	if isBeautiful(s):
		ans *= int(s, 2)
	else:
		nonBeautiful += [int(s, 10)]

ans = format(ans, 'b')
ans = int(ans, 10)
for x in nonBeautiful:
	ans *= x
print(ans)