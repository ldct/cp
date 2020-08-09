#!/usr/bin/env python3

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

def ans1(b):
    if b <= 1:
        return min(c, d)
    return d

def ans(a, b):
    if a == 0 and b == 0:
        return 0

    if a == 0 or b == 0:
        return ans1(a + b)

    if c == 1:
        if a == b:
            return c
        else:
            return c+d

    if d == 1:
        return 2*d

    if a == b:
        return min(c, 2*d)

    return min(c+d, 2*d)

print(ans(a, b))