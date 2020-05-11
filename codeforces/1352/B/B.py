#!/usr/bin/env python3

T = int(input())

def ans(n, k):
    if n % 2 == 1 and k % 2 == 0:
        return "NO"
    if n % 2 == 0 and k % 2 == 1:
        unit = 2
    else:
        unit = 1
    ans = [unit]*(k-1)
    n -= (unit*(k-1))
    if n <= 0:
        return "NO"
    return "YES\n" + ' '.join(str(x) for x in ans + [n])
    

for t in range(T):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    print(ans(n, k))