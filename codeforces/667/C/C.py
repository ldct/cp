#!/usr/bin/env pypy3

def ans(n,x,y):
	candidates = set()
	for gap in range(n-1,0,-1):
		if (y-x) % gap == 0:
			diff = (y-x) // gap

			ret = [y]
			for _ in range(n-1):
				ret += [ret[-1] - diff]
				if ret[-1] <= 0:
					ret = ret[:len(ret)-1]
					break
			ret = sorted(ret)
			while len(ret) < n:
				ret += [ret[-1] + diff]

			candidates.add(tuple(ret)[::-1])

	print(*min(candidates))
		
T = int(input())
for t in range(T):
	N,X,Y = input().split()
	X = int(X)
	Y = int(Y)
	N = int(N)

	ans(N,X,Y)