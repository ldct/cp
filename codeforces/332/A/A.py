#!/usr/bin/env python3

d1, d2, d3 = input().split()
d1 = int(d1)
d2 = int(d2)
d3 = int(d3)

a = 2*(d1 + d2)
b = (d1 + d2 + d3)
c = 2*(d1 + d3)
d = 2*(d2 + d3)

print(min(a, b, c, d))