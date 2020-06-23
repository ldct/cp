#!/usr/bin/env python3

def ans(a, b):
    ret = []
    b = set(b)
    for c in a:
        if c not in b:
            ret += [c]
    return ''.join(ret)

N = int(input())
ret = []
for _ in range(N):
    row = input().split(' ')
    row = [int(x) for x in row if len(x)]
    
    i = 0
    for r in row:
        if r != -1:
            i = i | r
    ret += [i]

print(sum(ret))