#!/usr/bin/env pypy3
	
N, D = input().split()
N = int(N)
D = int(D)

input()
speed = sum(map(int, input().split()))

import math

print(math.ceil(D / speed))