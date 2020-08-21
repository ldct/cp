#!/usr/bin/env pypy3

a, b, s, c, d, t = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
s = int(s)
t = int(t)

import sys

if a*d == b*c:
	print(0, 0)
else:
	det = a*d - b*c
	a,b,c,d = a/det, b/det, c/det, d/det
	a,b,c,d = d, -b, -c, a

	x = a*s + b*t
	y = c*s + d*t

	print(x, y)