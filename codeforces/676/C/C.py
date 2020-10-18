#!/usr/bin/env pypy3

def ans(S):
    N = len(S)

    print(3)

    print('L', 2)
    S = S[1] + S
    N = len(S)

    print('R', 2)
    S = S + S[1:N-1][::-1]
    N = len(S)

    print('R', N-1)
    S = S + S[N-2]

    assert(S == S[::-1])

ans(input())
