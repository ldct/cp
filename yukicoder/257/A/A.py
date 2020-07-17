#!/usr/bin/env pypy3

from math import gcd,sqrt

a, b = input().split(' ')
a = int(a)
b = int(b)

g = gcd(a, b)

if int(sqrt(g))**2 == g:
    print("Odd")
else:
    print("Even")