#!/usr/bin/env pypy3

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))

    seen = set()

    P = []
    for a in A:
        if a not in seen: 
            P += [a]
        seen.add(a)

    print(*P)