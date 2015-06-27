#!/usr/bin/env python3

n = input()
s = input()

n_o = len(list(i for i in s if i == '1'))
n_z = len(list(i for i in s if i == '0'))

print(max(n_o, n_z) - min(n_o, n_z))