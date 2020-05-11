#!/usr/bin/env python3

T = int(input())

def ans(n):
    if n <= 3:
        return "-1"
    if n % 3 == 2:
        left_peak = n
    else:
        left_peak = n - 1

    if left_peak % 3 == 0:
        left = list(range(2, left_peak+1, 3))
        left[-1] += 1
        mid = list(range(3, left_peak, 3))[::-1]
        right = list(range(1, n+1, 3))

        ans = left + mid + right + [n-2]
        return ' '.join(str(x) for x in ans)
    else:
        left = list(range(2, left_peak+1, 3))
        mid = list(range(3, left_peak, 3))[::-1]
        right = list(range(1, n, 3))

        adj = []
        if n % 3 == 0:
            adj = [n]

        ans = left + mid + right + adj
        return ' '.join(str(x) for x in ans)
    
for t in range(T):
    n = int(input())
    print(ans(n))