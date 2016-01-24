#!/usr/bin/env python3

from random import randint

N = 2000

print(str(N) + " -1 0 5 3")
for _ in range(N):
	print(str(randint(1, 100)) + " " + str(randint(1, 100)))