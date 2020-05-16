#!/usr/bin/env python3

import math

def ans(k): 
    if k < 4: return 0
    x = math.floor(
        (-7 + math.sqrt(49-12*(4-k))) / 6
    )
    return 1 + ans(k - (3*x*x + 7*x + 4))

T = int(input())
for t in range(T):
    n = int(input())
    print(ans(2*n))