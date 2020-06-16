#!/usr/bin/env python3
	
T = int(input())
for t in range(T):
	b = input()
	b = b[0] + b + b[-1]

	print(b[0:-1:2])
