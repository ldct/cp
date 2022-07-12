#!/usr/bin/env python3

import random

tem, num = [], 26267
random.seed(12)
print(1)
print()
print(200000, 1)
for i in range(10):
    for j in range(1, 2 * 10 ** 4 + 1):
        tem.append(j * num)

print(*tem)
print(1, 2)
