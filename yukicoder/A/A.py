#!/usr/bin/env python3

a, b, c, d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if a < b and c > d:
    print("YES")
else:
    print("NO")