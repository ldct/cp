#!/usr/bin/env python3
import sys

input()
arr = list(input().split())

ans = 1
for x in arr:
	ans *= int(x, 10)
print(ans)