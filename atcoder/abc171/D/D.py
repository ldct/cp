#!/usr/bin/env python3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()
    
input()
A = input().split(' ')
A = list(map(int, A))
Q = int(input())

curr_sum = sum(A)
curr_freqs = dict()

for a in A:
    if a not in curr_freqs: curr_freqs[a] = 0
    curr_freqs[a] += 1

for _ in range(Q):
    B, C = input().split(' ')
    B = int(B)
    C = int(C)

    if B not in curr_freqs:
        print(curr_sum)
        continue

    if C not in curr_freqs: curr_freqs[C] = 0

    curr_sum += (C - B)*curr_freqs[B]

    curr_freqs[C] += curr_freqs[B]
    curr_freqs[B] = 0


    print(curr_sum)



