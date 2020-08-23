#!/usr/bin/env python3

H = 10**3
W = 10**3

import random

print(H, W)
print(1, 1)
print(H, W)

for _ in range(H):
    print(''.join(random.choice(".") for _ in range(W)))