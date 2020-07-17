#!/usr/bin/env pypy3

from math import sin

def sinc(x):
    if abs(x) < 1e-10: return 1
    else:
        return sin(x)/x

partial_sum = 0

x = 0
j = 0

last_checkpoint = 0

while True: 
    s = sinc(x+j)**2
    partial_sum += s
    if j % 100 == 0: 
        if abs(partial_sum - last_checkpoint) < 1e-6: break
        print(partial_sum)
    j += 1