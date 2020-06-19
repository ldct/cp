#!/usr/bin/env pypy3

def ans(A):
    count = [0]*25
    for a in A:
        s = "{0:b}".format(a)
        s = list(s[::-1])
        for i, e in enumerate(s):
            if e == '1':
                count[i] += 1
    
    ret = 0
    while sum(count):
        next = [0]*25
        for i in range(25):
            if count[i] > 0:
                count[i] -= 1
                next[i] += 1
        next = ''.join(str(x) for x in next)
        next = int(next[::-1], 2)
        ret += next**2
    return ret

input()
A = input().split(' ')
A = [int(a) for a in A]

print(ans(A))