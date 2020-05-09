#!/usr/bin/env python3
#!/usr/bin/env python3

import math

def k_of_d(d):
    return d - 2**int(math.log(d, 2))

def ans(d, m):
    k = k_of_d(d)
    r0 = len(format(d,'b'))
    r = r0
    ans = 1
    while True:
        if r == 0:
            return (ans - 1) % m
        if r == r0:
            fac = (k + 2)
            ans *= fac
        else:
            fac = (2**(r-1)+1)
            ans *= fac
        r -= 1
        ans = ans % m

T = int(input())

for t in range(T):
    d, m = input().split(' ')
    d, m = int(d), int(m)
    print(ans(d, m))