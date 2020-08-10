#!/usr/bin/env pypy3

import math
from collections import Counter

def ok(c, side):
    if len(c) != side: return False
    for k in c:
        if c[k] != side: return False
    return True

input()

B = input().split()
B = list(map(int, B))

if True:
    import random
    B = [random.randint(1, 5) for _ in range(2*10**5)]

ret = 0

ub = math.floor(math.sqrt(len(B)))

if max(B) <= 2:
    ub = 3

count = 0

for side in range(1, ub+1):
    square = side*side

    # print("testing", side)

    c = Counter(B[:square])
    count += 1
    if ok(c, side):
        ret += 1

    i = 0
    j = square
    while j < len(B):
        c[B[i]] -= 1
        if c[B[i]] == 0:
            del c[B[i]]
        c[B[j]] += 1

        count += 1
        if ok(c, side):
            ret += 1

        i += 1
        j += 1

print(ret)
print(count)