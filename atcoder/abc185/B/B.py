#!/usr/bin/env pypy3

N, M, T = input().split()
N = int(N)
M = int(M)
T = int(T)

events = []

for _ in range(M):
    a, b = input().split()
    a = int(a)
    b = int(b)
    events += [(a, b)]

events += [(T, T+1)]

events = sorted(events)

def ans(N, events):
    charge = N
    last_time = 0

    for a, b in events:
        charge -= (a - last_time)
        if charge <= 0: return "No"
        charge += (b - a)
        if charge > N: charge = N
        last_time = b

    return "Yes"

print(ans(N, events))