#!/usr/bin/env python3

def num_squares(a, b):
  return a*(a+1)*((b-a) / 2 + (2*a+1) / 6)

print(num_squares(3, 5))