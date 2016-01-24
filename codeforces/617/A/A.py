#!/usr/bin/env python3

x = int(input())

print((x // 5) + (0 if x % 5 == 0 else 1))