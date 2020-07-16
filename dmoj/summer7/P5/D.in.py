#!/usr/bin/env pypy3

import random

N = 100

print(''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(N)))
print(''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(N)))