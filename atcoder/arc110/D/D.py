#!/usr/bin/env python3

from functools import lru_cache

MODULUS = 10**9+7
from functools import lru_cache

def choose(n,k,p=MODULUS):
    if k > n:
        return 0

    # calculate numerator
    num = 1
    for i in range(n,n-k,-1):
        num = (num*i)%p

    # calculate denominator
    denom = 1
    for i in range(1,k+1):
        denom = (denom*i)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * pow(denom,p-2,p))%p

@lru_cache(None)
def ans(M, A):
	if len(A) == 1:
		[a] = A
		ret = 0
		for x in range(a, M+1):
			ret += choose(x, a)
			ret %= MODULUS
		return ret

	if M < sum(A): return 0

	a = A[0]

	ret = 0
	for x in range(a, M+1):
		ret += choose(x, a)*ans(M-x, A[1:])
		ret %= MODULUS

	return ret

N, M = input().split()
A = tuple(map(int, input().split()))
N = int(N)
M = int(M)
print(ans(M, A))