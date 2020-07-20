#!/usr/bin/env pypy3

def gap(d, l, r):
	for b in range(l,r+1):
		c = b - d
		if l <= c <= r:
			return b,c
	assert(False)

def ans(l, r, m):
	for a in range(l,r+1):
		dist1 = m % a
		if dist1 <= (r - l) and m - dist1 > 0:
			b, c = gap(dist1, l, r)
			return a,b,c
		dist2 = a - m%a
		if dist2 <= (r - l):
			b, c = gap(-dist2, l, r)
			return a,b,c

T = int(input())
for _ in range(T):
	l, r, m = input().split(' ')
	l = int(l)
	r = int(r)
	m = int(m)
	print(*ans(l, r, m))