#!/usr/bin/env python3

def ok(N, a_array):
    for i in range(len(a_array)):
        a_array[i] = (a_array[i] + i) % N
    s = set(a_array)
    return N == len(set(s))

T = int(input())
for t in range(T):
    N = int(input())
    a_array = input().split(' ')
    a_array = list(int(x) for x in a_array)
    if ok(N, a_array):
        print('YES')
    else:
        print('NO')