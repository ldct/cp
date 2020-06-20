#!/usr/bin/env python3

T = int(input())

def ans(L, R):
    hours = R - L
    startAngle = -L*30
    endAngle = startAngle + (hours * 330)

    # print(startAngle, endAngle)
    # print([x for x in range(startAngle, endAngle+1) if x % 90 == 0])


    return len([x for x in range(startAngle, endAngle+1) if (x + 720) % 360 in [90, 270]])

for _ in range(T):
    [L, R, *rest] = input().split(' ')
    L = int(L)
    R = int(R)
    print(ans(L, R))