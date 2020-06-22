#!/usr/bin/env python3


input()
X = input().split(' ')
X = list(map(int, X))

P = round(sum(X)/len(X))

print(sum((x-P)**2 for x in X))
