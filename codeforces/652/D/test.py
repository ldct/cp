import array, __pypy__

TWO = 2
print(__pypy__.strategy([2**100 % 2]))
print(__pypy__.strategy([TWO**100 % 2]))
print(__pypy__.strategy([2**100 % TWO]))
print(__pypy__.strategy([pow(2, 100, TWO)]))
print(__pypy__.strategy(list(array.array('i', [2**100 % TWO]))))

A = [2**100]
A = [a % 2 for a in A]
print(__pypy__.strategy(A))
A = [__pypy__.intop.int_add(a,0) for a in A]
print(__pypy__.strategy(A))
