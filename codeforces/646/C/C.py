#!/usr/bin/env python3

from collections import defaultdict

T = int(input())

FIRST_PLAYER = "Ayush"
SECOND_PLAYER = "Ashish"

def ans(neighbours, x, n):
    if len(neighbours[x]) <= 1:
        return FIRST_PLAYER

    assert(n >= 3)

    n -= 3

    if n % 2 == 0:
        return SECOND_PLAYER
    
    return FIRST_PLAYER

for t in range(T):
    n, x = input().split(' ')
    x, n = int(x), int(n)
    neighbours = defaultdict(set)

    for _ in range(n-1):
        u, v = input().split(' ')
        u, v = int(u), int(v)
        
        neighbours[u].add(v)
        neighbours[v].add(u)

    print(ans(neighbours, x, n))