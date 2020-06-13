#!/usr/bin/env python3

n = int(input())

if n % 2 == 0:
    ret = ["2"]*(n // 2)
    print(len(ret))
    print(' '.join(ret))
else:
    n -= 3
    ret = ["3"] + ["2"]*(n // 2)
    print(len(ret))
    print(' '.join(ret))
