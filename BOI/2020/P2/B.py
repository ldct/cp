#!/usr/bin/env pypy3

import math

class vec3(tuple):

    @property 
    def x(self): return self[0]
    @property
    def y(self): return self[1]
    @property
    def z(self): return self[2]

    def __matmul__(v1, v2): return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    def __xor__(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.z * v2.x - v1.x * v2.z
        z = v1.x * v2.y - v1.y * v2.x
        return vec3((x, y, z))

    @staticmethod
    def triangle_area2(a, b, c):
        return ((a-b) ^ (a-c)).norm2()

    @staticmethod
    def coplanar(a, b, c):
        # the lines OB, OC, OA are coplanar
        return 0 == a @ (b ^ c)

    def norm2(self): return self @ self
    def norm(self): return math.sqrt(self.norm2)

    def __add__(self, v): return vec3((self.x + v.x, self.y + v.y, self.z + v.z))
    def __neg__(self): return vec3((-self.x, -self.y, -self.z))
    def __sub__(self, v): return self + (-v)

    def __mul__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            return vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __div__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        else:
            return vec3(self.x / v, self.y / v, self.z / v)

from decimal import Decimal
from itertools import combinations

S, P, G = input().split(' ')
S = int(S)
P = int(P)
G = int(G)

N = int(input())

arr = []

def sgn(x):
    if x == 0: return 0
    if x > 0: return 1
    return -1

def same_side(a,b,c,t):
    plane = a^b
    
    s1 = plane @ c
    s2 = plane @ t

    if s2 == 0: return False

    return sgn(s1) == sgn(s2)

from functools import lru_cache

@lru_cache(None)
def match3(a,b,c,t):
    a = vec3(a)
    b = vec3(b)
    c = vec3(c)
    t = vec3(t)
    return same_side(a,b,c,t) and same_side(b, c, a, t) and same_side(a,c,b,t)

@lru_cache(None)
def match2(a, b):
    # whether c is in the conical hull of a,b
    a = vec3(a)
    b = vec3(b)
    c = vec3((S, P, G))

    if not vec3.coplanar(a,b,c):
        return False

    a = a^c
    b = c^b

    return a @ b >= 0

@lru_cache(None)
def match1(a):

    (s,p,g) = a

    if S == 0 and s == 0:
        ss = None
    elif S == 0 or s == 0:
        return False
    else:
        ss = Decimal(s) / Decimal(S)

    if P == 0 and p == 0:
        pp = None
    elif P == 0 or p == 0:
        return False
    else:
        pp = Decimal(p) / Decimal(P)

    if G == 0 and g == 0:
        gg = None
    elif G == 0 or g == 0:
        return False
    else:
        gg = Decimal(g) / Decimal(G)


    cmp = [ss,pp,gg]
    cmp = [x for x in cmp if x is not None]

    assert(len(set(cmp)) > 0)
    return len(set(cmp)) == 1

def ans():
    for a in arr:
        if a is None: continue
        if match1(a):
            return 1
    for a, b in combinations(arr, 2):
        if a is None or b is None: continue
        if match2(a, b):
            return 2
    for a, b, c in combinations(arr, 3):
        if a is None or b is None or c is None: continue
        if match3(a,b,c,(S,P,G)):
            return 3
    return 0

if False:
    import random
    S,P,G = 100,77,88
    for i in range(500):
        s = random.randint(1,500)
        p = random.randint(1,500)
        g = random.randint(1,500)

        arr += [(s,p,g)]

        print(i, ans())

for _ in range(N):
    lst = input().split(' ')

    if lst[0] == 'A':
        [s, p, g] = lst[1:]
        s = int(s)
        p = int(p)
        g = int(g)

        arr += [(s, p, g)]
    elif lst[0] == 'R':
        arr[int(lst[1]) - 1] = None
    
    print(ans())
