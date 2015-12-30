#!/usr/bin/env python3

import random

n = 100000
h_u = [random.randint(0, n) for i in range(n)]
h_s = sorted(h_u)

print(len(h_u))
print(' '.join(str(i) for i in h_u))