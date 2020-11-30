#!/usr/bin/env python3

A, B, X, Y = input().split()

a = int(A)
b = int(B)
x = int(X)
y = int(Y)

def ans(a, b, x, y):
	diag = x
	cross = x
	ud = y
	for _ in range(100):
		ud = min(ud, cross + diag)
		cross = min(cross, ud + diag)
		diag = min(diag, ud + cross)

	if a <= b:
		return (cross + ud*(b-a))
	else:
		return (cross + ud*(a - b - 1))


print(ans(a, b, x, y))