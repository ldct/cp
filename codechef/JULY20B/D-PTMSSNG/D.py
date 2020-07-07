#!/usr/bin/env pypy3

T = int(input())

def ans(points):
    ans_x = 0
    ans_y = 0

    for x, y in points:
        ans_x ^= x
        ans_y ^= y
    
    return (ans_x, ans_y)

for _ in range(T):
    N = int(input())
    points = []
    for _ in range(4*N - 1):
        x, y = input().split(' ')
        x = int(x)
        y = int(y)
        points += [(x, y)]
    print(*ans(points))
