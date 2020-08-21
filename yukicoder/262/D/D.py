#!/usr/bin/env pypy3

a, b, c, d, e, f = input().split()
a = int(a)
assert(a > 0)

b = int(b)
if a != b:
	import sys
	print(0)
	sys.exit(0)
	
b /= a

c = int(c) / a
d = int(d) / a
e = int(e) / a
f = int(f) / a

f -= e

x0 = c/(-2)
y0 = d/(-2)

rr = f + x0**2 + y0**2

import math
print(math.sqrt(rr))
