#!/usr/bin/env pypy3

def ans(X):
    if X == 0: return 0
    X = X % (bin(X).count('1'))
    return 1+ans(X)

# test case injection
if False:
    import random
    X = ''.join(random.choice("1") for _ in range(2*10**5))
    N = len(X)
    # print(N, X)
    # exit(0)
else:
    N = int(input())
    X = input()

N = N-1

popcount = X.count('1')
X_int = int(X, 2)

import array

two_pow_mod_pc_plus = array.array('i', [0]*(N+1))
two_pow_mod_pc_minus = array.array('i', [0]*(N+1))

two_pow_mod_pc_plus[0] = 1 % (popcount+1)
if popcount <= 1:
    two_pow_mod_pc_minus[0] = 0
else:
    two_pow_mod_pc_minus[0] = 1 % (popcount-1)

for i in range(1, len(two_pow_mod_pc_plus)):
    two_pow_mod_pc_plus[i] = (2*two_pow_mod_pc_plus[i-1]) % (popcount+1)

for i in range(1, len(two_pow_mod_pc_minus)):
    if popcount <= 1:
        two_pow_mod_pc_minus[i] == 1
    else:
        two_pow_mod_pc_minus[i] = (2*two_pow_mod_pc_minus[i-1]) % (popcount-1)

X_mod_pc_plus = X_int % (popcount+1)
if popcount <= 1:
    X_mod_pc_minus = 0
else:
    X_mod_pc_minus = X_int % (popcount-1)

for i, x in enumerate(X):
    # if i % 1000 == 0: print(i)
    if x == '0':
        r = 1 + ans((X_mod_pc_plus + two_pow_mod_pc_plus[N-i]) % (popcount+1))
    else:
        if popcount == 1:
            print(0)
            continue
        else:
            r = 1 + ans((X_mod_pc_minus - two_pow_mod_pc_minus[N-i]) % (popcount-1))
    print(r)
