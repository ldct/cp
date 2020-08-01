#!/usr/bin/env python3

def fprint(*args):
	print(*args, flush=True)

N, K = input().split()
N = int(N)
K = int(K)
assert(K == 1)

available = set(range(1,N+1))

if N % 2 == 1:
	fprint("First")
	fprint(1)
	available.remove(1)
else:
	fprint("Second")

while True:
	r = abs(int(input()))
	if r not in available:
		import sys
		sys.exit(0)
	available.remove(r)

	fprint(available.pop())
