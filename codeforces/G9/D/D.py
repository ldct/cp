#!/usr/bin/env python3

def mex(A):
    A = set(A)
    for i in range(1001):
        if i not in A: return i
    assert(False)

def ans(A):
    ops = []

    while True:
        m = mex(A)
        if 0 <= m < len(A):
            ops += [m]
            A[m] = m
        else:
            assert(m == len(A))
            if sorted(A) == A:
                break
            for i in range(len(A)):
                if i != A[i]:
                    ops += [i]
                    A[i] = m
                    break
    assert(len(ops) <= 2*len(A))
    print(len(ops))
    print(' '.join(str(x+1) for x in ops))

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    ans(A)