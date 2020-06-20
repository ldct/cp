#!/usr/bin/env python3

def lucky(s):
    s = str(s)
    for i in range(0, 10):
        if str(i) not in "47" and str(i) in s:
            return False
    return True

def ans(n):
    for i in range(2, n+1):
        if not n % i == 0: continue
        if lucky(i): return "YES"
    return "NO"

n = int(input())
print(ans(n))
