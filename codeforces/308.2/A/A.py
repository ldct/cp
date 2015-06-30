#!/usr/bin/env python3

N = int(input())

ans = 0

for n in range(N):
	i, j, a, b = tuple(map(int, input().split(' ')))
	ans += (a - i + 1) * (b - j + 1)

print(ans)
