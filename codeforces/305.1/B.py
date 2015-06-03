#!/usr/bin/env python3

N = input()
N = int(N)
A = input().split(' ')
A = list(map(int, A))

def get_L(A):
    L_candidates = [] # increasing list of indices with A smaller than anything considered so far
    L = A[:]

    for i in range(len(A)):
        while L_candidates and A[L_candidates[-1]] >= A[i]:
            L_candidates.pop()
        if L_candidates:
            L[i] = L_candidates[-1]
        else:
            L[i] = -1
        L_candidates.append(i)
    return L

L = get_L(A)
R = [N - x - 1 for x in get_L(A[::-1])][::-1]

strengths = [0] * (N + 3)
for i in range(N):
    p = R[i] - L[i] - 1
    strengths[p] = max(strengths[p], A[i])

strengths = strengths[1:N+1]

for i in range(N-1)[::-1]:
    strengths[i] = max(strengths[i], strengths[i+1])

print(' '.join(map(str, strengths)))