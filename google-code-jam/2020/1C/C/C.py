#!/usr/bin/env python3

def solution(D, angles):
	for a in angles:
		if angles.count(a) >= D: return 0
	if D == 2:
		return 1
	if D == 3:
		# cut one in half
		for a in angles:
			if 2*a in angles:
				return 1
		
		# shave one thing off
		for a in angles:
			if angles.count(a) == 2:
				for j in angles:
					if j > a:
						return 1
	return 2


T = int(input())
for t in range(T):
	N, D = input().split(' ')
	D = int(D)
	angles = list(int(x) for x in input().split(' '))

	sol = solution(D, angles)

	print("Case #" + str(t+1) + ": " + str(sol))
