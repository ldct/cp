#!/usr/bin/env python3

def ans(a, b):
	if b/2 > a: return a
	if a/2 > b: return b
	return (a + b) // 3


T = int(input())
for t in range(T):
	a, b = input().split(' ')
	a = int(a)
	b = int(b)

	print(ans(a, b))