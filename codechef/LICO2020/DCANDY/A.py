#!/usr/bin/env python3

T = int(input())

def ans(candies):
    candies = sorted(candies)[::-1]
    ret = 0
    i = 2
    while i < len(candies):
        ret += candies[i]
        i += 3
    return ret


for _ in range(T):
    N = int(input())
    candies = input().split(' ')
    candies = [int(x) for x in candies if len(x)]

    print(ans(candies))
