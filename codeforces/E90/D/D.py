#!/usr/bin/env pypy3

from sys import stdin, stdout
import array
 
def input():
    return stdin.readline().strip()

def maxSum(A): 
      
    max_so_far = 0
    max_ending_here = 0
      
    for a in A: 
        max_ending_here = max_ending_here + a
        if max_ending_here < 0: 
            max_ending_here = 0 
        elif (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
              
    return max_so_far 

def ans(A):
    
    base = 0
    i = 0

    a1 = array.array('q')
    a2 = array.array('q')

    while i < len(A):
        base += A[i]
        if i+1 < len(A):
            a1.append(A[i+1] - A[i])
        i += 2

    i = 1
    while i < len(A):
        if i+1 < len(A):
            a2.append(A[i] - A[i+1])
        i += 2
    
    return base + max(maxSum(a1), maxSum(a2))

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(ans(A))
