#!/usr/bin/env pypy3

def ok(n):
    if "7" in str(n): return False
    if "7" in oct(n): return False
    return True

def ans(N):
    ret = 0
    for x in range(1,N+1):
        if ok(x):
            ret += 1
    return ret

print(ans(int(input())))
