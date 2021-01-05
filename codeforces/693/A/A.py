#!/usr/bin/env pypy3

def ans(w, h, n):
	num_pieces = 1
	while w % 2 == 0:
		w = w // 2
		num_pieces *= 2
	while h % 2 == 0:
		h = h // 2
		num_pieces *= 2

	if num_pieces >= n:
		return "YES"
	return "NO"

for _ in range(int(input())):
	[w, h, n] = list(map(int, input().split()))
	print(ans(w, h, n))