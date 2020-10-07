#!/usr/bin/env python3

import random

N = 10**5
print(N)
print(' '.join(str(random.randint(-4000, 4000)) for _ in range(N)))