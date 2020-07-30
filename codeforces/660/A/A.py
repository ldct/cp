#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(n):
	a = 2*3
	b = 2*5
	c = 2*7
	d = n - (a+b+c)

	if d <= 0:
		return False
	elif len(set([a,b,c,d])) == 4:
		return (a,b,c,d)
	else:
		c = 3*5
		d = n - (a+b+c)
		if d <= 0:
			return False
		else:
			assert(len(set([a,b,c,d])) == 4)
			return (a,b,c,d)

T = int(input())

for _ in range(T):
	n = int(input())
	r = ans(n)
	if not r:
		print("NO")
	else:
		print("YES")
		print(*r)
