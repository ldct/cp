#!/usr/bin/env python3

a1, a2 = input().split()
a1, a2 = int(a1), int(a2)

time = 0
while a1 > 0 and a2 > 0:
	if a1 < a2:
		a1 += 1
		a2 -= 2
	else:
		a1 -= 2
		a2 += 1
	if a1 >= 0 and a2 >= 0:
		time += 1

print(time)