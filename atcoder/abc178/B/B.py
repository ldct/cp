#!/usr/bin/env pypy3

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

print(max(a*c, a*d, b*c, b*d))