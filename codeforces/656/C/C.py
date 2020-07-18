#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

def ans(A):
    A += [float("-inf")]
    i = len(A)-1

    while i > 0 and A[i-1] >= A[i]:
        i -= 1

    while i > 0 and A[i-1] <= A[i]:
        i -= 1

    return i

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))

    print(ans(A))