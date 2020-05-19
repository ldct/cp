#!/usr/bin/env python3

import math

T = int(input())

def ans(a, b, c, d):
	if b >= a:
		return b
	if d >= c:
		return -1
	a -= b
	return b + c * math.ceil(a / (c - d))

for t in range(T):
	a, b, c, d = input().split(' ')
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	print(ans(a, b, c, d))