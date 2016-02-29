#!/usr/bin/env python3

import math

RATE = 1.000000011

s, t = input().split(' ')
s, t = int(s), int(t)

print(s * RATE**t)
