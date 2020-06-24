#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()
    

def ans(A, W):
    A = sorted(A)[::-1]
    W_1 = 0
    W_rest = []

    for w in W:
        if w == 1:
            W_1 += 1
        else:
            W_rest += [w]

    ret = 2*sum(A[0:W_1])
    
    A = A[W_1:]
    W = W_rest
    
    # greedily populate the maxima
    ret += sum(A[0:len(W)])
    A = A[len(W):]
    W = [w-1 for w in W]

    W = sorted(W)[::-1]
    A = A[::-1]

    w_sum = 0
    for w in W:
        ret += A[w_sum]
        w_sum += w

    return ret

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    W = input().split(' ')
    W = list(map(int, W))

    print(ans(A, W))