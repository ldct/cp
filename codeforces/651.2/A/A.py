#!/usr/bin/env pypy3

import math

class Sieve:
    def __init__(self, n=10**7):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i): 
                if j > i: s[j] = i
        self.s = s
    
    def primes():
        return [i for i, e in enumerate(self.s) if e == -1 and i >= 2]

    def fastfactorize(self, n):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            ret += [self.s[n]]
            n = n // self.s[n]

        ret += [n]

        return ret

sieve = Sieve(10**6+1)

at = [sorted(sieve.fastfactorize(i))[1:] for i in range(10**6+1)]

for i in range(len(at)):
    if len(at[i]) == 0:
        at[i] = 1
    else:
        a = 1
        for aa in at[i]:
            a *= aa
        at[i] = a


prefix = [1]

for i in range(1,len(at)):
    prefix += [max(prefix[-1], at[i])]

def ans2(n):
    ret = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            ret = max(ret, math.gcd(a, b))
    return ret
        
T = int(input())

for _ in range(T):
    N = int(input())
    print(prefix[N])
