#!/usr/bin/env python3

def ans(s):
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1
    s = s[i:][::-1]

    k = 0
    while k < len(s) and s[k] == '1':
        k += 1
    s = s[k:][::-1]

    j = s.count("10")

    if j == 0:
        return '0'*i + '1'*k

    return '0'*(i+1) + '1'*k

    return (i, j, k)
    

    
T = int(input())

for _ in range(T):
    input()
    s = input()
    print(ans(s))
