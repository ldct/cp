#!/usr/bin/env python3

def ans(A, B, K):
    pA = [0]
    for a in A:
        pA += [pA[-1] + a]
    pB = [0]
    for b in B:
        pB += [pB[-1] + b]

    # print(pA, pB)

    j = len(B)

    ans = float("-inf")

    for i in range(0, len(pA)):
        # print("considering", i, j)
        while j > 0 and pA[i] + pB[j] > K: j -= 1
        if pA[i] + pB[j] <= K:
            ans = max(ans, i + j)

    return ans

N, M, K = input().split(' ')
K = int(K)

A = input().split(' ')
A = list(map(int, A))

B = input().split(' ')
B = list(map(int, B))

print(ans(A, B, K))