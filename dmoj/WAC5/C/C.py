#!/usr/bin/env pypy3

from collections import Counter
import array

import math
if False:
    import random
    B = [random.randint(1, 2*10**5-10) for _ in range(2*10**5)]
    ub = math.floor(math.sqrt(len(B)))
else:
    input()
    B = input().split()
    B = list(map(int, B))


ret = 0

ub = math.floor(math.sqrt(len(B)))

if max(B) <= 2:
    ub = 3

for side in range(1, ub+1):
    square = side*side
    # print("checking", square)

    freqs = [0]*(len(B)+1)

    num_side = 0

    for b in B[:square]:
        if freqs[b] == side-1:
            num_side += 1
        elif freqs[b] == side:
            num_side -= 1
        freqs[b] += 1
    
    if num_side == side:
        ret += 1

    i = 0
    j = square
    while j < len(B):

        # decrement B[i]
        b = B[i]
        if freqs[b] == side+1:
            num_side += 1
        elif freqs[b] == side:
            num_side -= 1
        freqs[b] -= 1

        # increment B[j]
        b = B[j]
        if freqs[b] == side-1:
            num_side += 1
        elif freqs[b] == side:
            num_side -= 1
        freqs[b] += 1

        if num_side == side:
            ret += 1

        i += 1
        j += 1

print(ret)