#!/usr/bin/env python3
import sys

X = int(input())
b2 = "{0:b}".format(X)
print(sum(1 for s in b2 if s == '1'))