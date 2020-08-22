#!/usr/bin/env pypy3

def fit(x):
	ret = 0

	while ret <= x:
		x -= ret
		ret += 1

	return ret-1

def ans(a, b, c):
	if a > b: return ans(b, a, c)
	
	gap = b-a
	fill = min(gap, c)

	c -= fill
	a += fill

	if c > 0:
		assert(a == b)
		a += c // 2
		b += c // 2

	x = min(a, b)

	return fit(x)



a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(ans(a,b,c))