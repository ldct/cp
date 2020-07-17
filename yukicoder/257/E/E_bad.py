#!/usr/bin/env pypy3

import cmath

x = float(input())
i = 1j
ix = i*x

pos_term = cmath.exp(-ix)*cmath.log(1 - cmath.exp(-i))
neg_term = cmath.exp(+ix)*cmath.log(1 - cmath.exp(+i))
print((pos_term - neg_term)/(2*i))