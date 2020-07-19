#!/usr/bin/env pypy3

from math import sqrt, pi, atan2, cos, sin

def ans(tx, ty, x, y, k):
	dx = x - tx
	dy = y - ty
	r = sqrt(dx**2 + dy**2)

	angle = atan2(dy, dx)
	delta_angle = 2*pi / k

	for _ in range(k-1):
		angle += delta_angle
		x = tx + r*cos(angle)
		y = ty + r*sin(angle)
		print(f"{x:.10f} {y:.10f}")

T = int(input())

for _ in range(T):
	tx, ty, x, y, k = input().split(' ')
	tx = int(tx)
	ty = int(ty)
	x = int(x)
	y = int(y)
	k = int(k)
	ans(tx, ty, x, y, k)