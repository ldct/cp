#!/usr/bin/env python3

N = int(input())
X = list(map(int, input().split(' ')))

def min_cost(i):
    if i == 0:
        return X[1] - X[0]
    if i == N-1:
        return X[N-1] - X[N-2]
    return min(X[i] - X[i-1], X[i+1] - X[i])

def max_cost(i):
    return max(X[i] - X[0], X[N-1] - X[i])

for i, x in enumerate(X):
    print(min_cost(i), max_cost(i))