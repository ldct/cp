#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_tuple(): return input().split()
def read_int(): return int(input())

import math

### CODE HERE

def gsd(R, a, b):
    x_A, y_A, z_A = a
    x_B, y_B, z_B = b
    return abs(x_A - x_B)

    dist = math.sqrt((x_B-x_A)**2+(y_B-y_A)**2+(z_B-z_A)**2)
    phi = math.asin((dist/2/R))
    return 2*phi*R

N, M, R, T, K = read_int_tuple()
airports = read_int_list()
airports = set([c-1 for c in airports])

fastest_airport = [10.0*R] * N
city_positions = []
cases = []

for _ in range(N):
    v, x, y, z = read_tuple()
    cases += [int(v)]
    city_positions += [(float(x), float(y), float(z))]

for i in range(N):
    if i in airports:
        fastest_airport[i] = 0.0

for _ in range(M):
    a, b = read_int_tuple()
    a -= 1
    b -= 1

    dist = gsd(R, city_positions[a], city_positions[b])

    if a in airports:
        print("updating f", b)
        fastest_airport[b] = min(fastest_airport[b], dist)
    if b in airports:
        print("updating f", a)
        fastest_airport[a] = min(fastest_airport[a], dist)

print(fastest_airport)

ret = -1
for i in range(N):
    dist1 = gsd(R, city_positions[0], city_positions[i])
    dist_total = dist1 + fastest_airport[i]
    if dist_total < T-10**-3:
        ret = max(ret, cases[i])

print(ret)