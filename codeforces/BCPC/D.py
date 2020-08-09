#!/usr/bin/env pypy3
import sys
print('\n'.join("Neither" if n==1 else "Prime" if all(n%f!=0 for f in range(2,1+int(n**0.5))) else "Composite" for n in map(int,sys.stdin.readlines()[1:])))
