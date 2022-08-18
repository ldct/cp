#!/usr/bin/env python3

from random import randint

T = 1
N = 20

print(T)
for _ in range(T):
    print(N)
    print(*list([randint(1, 500) for i in range(N)]))