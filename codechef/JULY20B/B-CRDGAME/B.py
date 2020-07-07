#!/usr/bin/env pypy3

def power(n):
    n = str(n)
    return sum(int(c) for c in n)

T = int(input())

for _ in range(T):
    N = int(input())
    A_points = 0
    B_points = 0
    for _ in range(N):
        A, B = input().split(' ')
        A = int(A)
        B = int(B)

        p_A = power(A)
        p_B = power(B)

        if p_A >= p_B:
            A_points += 1
        if p_B >= p_A:
            B_points += 1

    if A_points > B_points:
        print(0, max(A_points, B_points))
    elif B_points > A_points:
        print(1, max(A_points, B_points))
    else:
        print(2, max(A_points, B_points))
