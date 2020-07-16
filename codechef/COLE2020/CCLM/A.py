#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A):
    for a in A:
        if a % 2 == 0: return "NO"
    return "YES"
    
T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(ans(A))