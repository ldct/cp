#!/usr/bin/env pypy3

def ans(fishes):
    if len(set(fishes)) == 1:
        return -1
    target = max(fishes)

    for i in range(len(fishes)):
        if fishes[i] == target and i+1 < len(fishes) and fishes[i+1] < target: return 1+i
        if fishes[i] == target and i-1 >= 0 and fishes[i-1] < target: return 1+i
    return '?'

for _ in range(int(input())):
    input()
    fishes = list(map(int, input().split()))
    print(ans(fishes))