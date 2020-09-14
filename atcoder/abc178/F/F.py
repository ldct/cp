#!/usr/bin/env pypy3

def ans(N, A, B):
    B = B[::-1]

    match_vals = set()

    for i in range(N):
        if A[i] == B[i]:
            match_vals.add(A[i])

    if len(match_vals) == 0:
        print("Yes")
        print(*B)
        return

    assert(len(match_vals) == 1)
    [m] = list(match_vals)

    ok = []
    bad = []
    for i in range(N):
        if B[i] != m and A[i] != m:
            ok += [i]
        if A[i] == B[i]:
            bad += [i]

    if len(bad) > len(ok):
        print('No')
        return

    for i in range(len(bad)):
        B[bad[i]], B[ok[i]] = B[ok[i]], B[bad[i]]

    print('Yes')
    print(*B)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans(N, A, B)