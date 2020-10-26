#!/usr/bin/env pypy3

def ans2(x):
    ret = 0
    for i in range(x+1):
        ret += i
    return ret

def ans(x):
    d = int(str(x)[0])
    return (d-1)*10 + ans2(len(str(x)))

for _ in range(int(input())):
    x = int(input())
    print(ans(x))