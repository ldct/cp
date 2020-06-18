#!/usr/bin/env python3

fibs = [0, 1]

while fibs[-1] < 10**9:
    fibs += [fibs[-1] + fibs[-2]]

def ans(N):
    if N == 0:
        return '0 0 0'
    if N == 1:
        return '1 0 0'
    
    i = fibs.index(N)
    return f"{fibs[i-2]} {fibs[i-2]} {fibs[i-3]}"

N = int(input())
print(ans(N))
