#!/usr/bin/env pypy3
import sys
def ans(q,n,l): return min(q,n**l)*l+(0 if n**l>=q else ans(q-min(q,n**l),n,l+1))
print('\n'.join(str(ans(q,n,1)) for q,n in [map(int, a.split()) for a in sys.stdin.readlines()[1:]]))