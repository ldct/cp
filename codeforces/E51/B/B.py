#!/usr/bin/env python3

l, r = input().split(' ')
l = int(l)
r = int(r)

print("YES")

i = l

while i+1 <= r:
    print(i, i+1)
    i += 2