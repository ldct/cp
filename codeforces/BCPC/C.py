#!/usr/bin/env pypy3
import sys
print('\n'.join("NO" if all(y-x>=a[1] for x,y in zip(sorted(b),sorted(b)[1:])) else "YES" for a,b in zip(*[iter([list(map(int,r.split())) for r in sys.stdin.readlines()[1:]])]*2)))
