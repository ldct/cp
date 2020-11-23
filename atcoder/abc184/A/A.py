#!/usr/bin/env python3

def det(lst):
    a, b, c, d = lst
    return a*d - b*c

a, b = input().split()
c, d = input().split()

print(det(map(int, [a, b, c, d])))