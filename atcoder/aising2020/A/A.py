#!/usr/bin/env python3

import math

L, R, d = input().split(' ')
L = int(L)
R = int(R)
d = int(d)

small = math.ceil(L / d)
big = R // d

print(big - small + 1)