#!/usr/bin/env python3

N, X, T = input().split()
N = int(N)
X = int(X)
T = int(T)

import math
print(T*math.ceil(N/X))