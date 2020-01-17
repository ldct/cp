#!/usr/bin/env python3

import re
t = int(input())

def score(match):
    a, b = match.span()
    return b-a-1

def ans(str):
    return max((score(match) for match in re.finditer(r'AP+', str)), default=0)

for i in range(t):
    input()
    s = input()
    print(ans(s))