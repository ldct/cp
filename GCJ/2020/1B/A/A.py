from functools import reduce

def powers(upto):
    for i in range(upto):
        yield 2**i

def fourths(n):
    if n == 0:
        return [[]]
    ret = []
    for possibility in fourths(n-1):
        ret.append([1] + possibility)
        ret.append([-1] + possibility)
        ret.append([0] + possibility)
    return ret

def prod(a, t):
    return tuple(a * x for x in t)

def add_tuples(j, k):
    return j+k

def prefix_powers(n):
    for i in range(0, n+1):
        yield list(powers(i)) + [0]*(n-i)

def possible_visits(n):
    for p in prefix_powers(n):
        for possibility in fourths(n):
            yield tuple(a*b for a, b in list(zip(p, possibility)))

for v in sorted(set(possible_visits(9))):
    if sum(v) == 5:
        print(v)