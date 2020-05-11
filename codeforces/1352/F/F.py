#!/usr/bin/env python3

T = int(input())

def compute_n(s):
    n0 = 0
    n1 = 0
    n2 = 0

    for i in range(len(s)-1):
        p = s[i:i+2]

        if p == "00": n0 += 1
        elif p == "11": n2 += 1
        else: n1 += 1

    return (n0, n1, n2)

def ans(n0, n1, n2):
    ret = ""
    num_domains = n1 + 1
    if num_domains  == 1:
        assert n0 * n2 == 0
        if n0 == 0:
            return "1"*(n2+1)
        elif n2 == 0:
            return "0"*(n0+1)
    ret += "0"*(n0+1)
    ret += "1"*(n2+1)
    num_domains -= 2

    next = 0

    while num_domains > 0:
        ret += str(next)
        next = 1 - next
        num_domains -= 1
    
    return ret
    
for t in range(T):
    n0, n1, n2 = input().split(' ')
    n0 = int(n0)
    n1 = int(n1)
    n2 = int(n2)

    r = ans(n0, n1, n2)
    print(r)