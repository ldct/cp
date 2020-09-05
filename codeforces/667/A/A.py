#!/usr/bin/env pypy3

import math

T = int(input())
for t in range(T):
	A, B = input().split()
	A = int(A)
	B = int(B)
	print(math.ceil(abs(B-A)/10))