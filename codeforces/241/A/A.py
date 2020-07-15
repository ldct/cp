#!/usr/bin/env pypy3

N = int(input())

lb = float("-inf")
ub = float("+inf")

def flip(sign):
    if sign == ">=": return '<'
    if sign == "<": return '>='
    if sign == ">": return '<='
    if sign == "<=": return '>'

for _ in range(N):
    sign, x, ans = input().split(' ')
    x = int(x)

    if ans == 'N':
        sign, ans = flip(sign), 'Y'

    assert(ans == 'Y')

    if sign == ">=": lb = max(lb, x)
    if sign == ">": lb = max(lb, x+1)
    if sign == "<=": ub = min(ub, x)
    if sign == "<": ub = min(ub, x-1)

if lb <= ub:
    if lb == float("-inf"): 
        print(ub)
    else:
        print(lb)
else:
    print("Impossible")