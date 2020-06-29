#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(n):
    count2 = 0
    count3 = 0

    while n % 2 == 0:
        n = n // 2
        count2 += 1
    
    while n % 3 == 0:
        n = n // 3
        count3 += 1

    if n > 1:
        return -1

    if count2 > count3:
        return -1

    return (count3 - count2) + count3

    return '?'

T = int(input())

for _ in range(T):
    n = int(input())
    print(ans(n))