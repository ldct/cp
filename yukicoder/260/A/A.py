#!/usr/bin/env pypy3

import math

def fprint(*args):
	print(*args, flush=True)

N = int(input())

if N % 2 == 0:
	fprint(2, math.ceil(N/2))
else:
	fprint(1, math.ceil(N/2))

while True:
	status = int(input())
	if status == 0:
		break
	elif status == 3:
		a, b = input().split()
		a = int(a)
		b = int(b)
		assert(a in [1, 2])
		if a == 2:
			b += 1
		fprint(a, N+1-b)
	else:
		assert(False)
