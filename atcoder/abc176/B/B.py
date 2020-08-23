#!/usr/bin/env python3

N = input()

sum_digits = 0

for c in N:
    sum_digits += int(c)
    sum_digits %= 9

if sum_digits == 0:
    print('Yes')
else:
    print('No')