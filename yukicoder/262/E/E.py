#!/usr/bin/env pypy3

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

discr = b**2 - 4*a*c

if discr < 0:
	print("imaginary")
elif discr == 0:
	print(-b / (2*a))
else:
	import math
	r1 = (-b + math.sqrt(discr)) / (2*a)
	r2 = (-b - math.sqrt(discr)) / (2*a)
	r1, r2 = sorted([r1, r2])
	print(r1, r2)