#!/usr/bin/env pypy3

def ans(a, b):
    if a < b:
        return ans(b, a)

    a = bin(a)[2:]
    b = bin(b)[2:]

    while len(b) != len(a):
        b = "0" + b

    ret = []
    for i in range(len(a)):
        if a[i] == b[i]:
            ret += "0"
        else:
            ret += "1"

    return int(''.join(ret), 2)

for _ in range(int(input())):
    a, b = input().split()
    print(ans(int(a), int(b)))
