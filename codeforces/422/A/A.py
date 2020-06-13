#!/usr/bin/env python3

import math

A, B = input().split(' ')
A = int(A)
B = int(B)

x = min(A, B)

print(math.factorial(x))
