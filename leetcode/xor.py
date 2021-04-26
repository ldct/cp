#!/usr/bin/env pypy3

import random

for _ in range(10000):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)

    if ((a & b) ^ (a & c)) != (a & (b ^ c)):
        print(a, b, c)

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
