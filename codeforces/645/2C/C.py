#!/usr/bin/env python3

T = int(input())

def ans(x1, y1, x2, y2):
	x = x2 - x1 + 1
	y = y2 - y1 + 1

	return (x-1)*(y-1) + 1

for t in range(T):
	x1, y1, x2, y2 = input().split(' ')
	x1 = int(x1)
	y1 = int(y1)
	x2 = int(x2)
	y2 = int(y2)
	print(ans(x1, y1, x2, y2))