#!/usr/bin/env python3

from itertools import permutations

def ans(x, y, z):
    old_xyz = [x, y, z]

    if len(set([x, y, z])) == 1:
        print("YES")
        print(x, x, x)
        return
    if len(set([x, y, z])) == 3:
        print("NO")
        return
    # two are the same
    l = sorted([x, y, z])
    [x, y, z] = l

    if x == y:
        print("NO")
        return

    assert(y == z)

    for a, b, c in permutations([x, z, x]):
        if [max(a,b), max(a,c), max(b,c)] == old_xyz:
            print("YES")
            print(a, b, c)
            return

    assert(False)
    
T = int(input())

for _ in range(T):
    x, y, z = input().split(' ')
    x = int(x)
    y = int(y)
    z = int(z)
    ans(x, y, z)