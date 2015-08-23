#!/usr/bin/env python3

n, m = input().split(' ')
n = int(n)
m = int(m)

left_range = m - 1
right_range = n - m

if (left_range == 0 and right_range == 0):
    print(1)
elif (left_range == 0):
    print(m + 1)
elif (right_range == 0):
    print(m - 1)
elif (left_range < right_range):
    print(m + 1)
else:
    print(m - 1)