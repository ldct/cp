#!/usr/bin/env python3

from collections import defaultdict

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Matrix(list):
    def __matmul__(self, B) :
        A = self
        return Matrix([[min(1,sum(A[i][k]*B[k][j] for k in range(len(B))))
                    for j in range(len(B[0])) ] for i in range(len(A))])

    def __pow__(self, n, modulus=None):
        assert(modulus is None)

        result = Matrix.Identity(len(self))
        b = self
        while n > 0:
            if (n%2) == 0:
                b = b @ b
                n //= 2
            else:
                result = b @ result
                b = b @ b
                n //= 2
        return result

    @classmethod  
    def Identity(cls, size):
        size = range(size)
        return Matrix([[(i==j)*1 for i in size] for j in size])

class Solution:
    def intersects(self, i, j, k, l):
        if j < k: return False
        if i > l: return False
        return True
    def is_root(self, c):
        reachable_from_c = set(self.reachable[c])
        for d in reachable_from_c:
            if set(self.reachable[d]) != reachable_from_c: return False
        return True
    def maxNumOfSubstrings(self, s):
        left = defaultdict(lambda : float("inf"))
        right = defaultdict(lambda : float("-inf"))
        for i, c in enumerate(s):
            left[c] = min(left[c], i)
            right[c] = max(right[c], i)
            
        intervals = dict()
        for c in left:
            intervals[c] = (left[c], right[c])
            
        adjacency = []
        for _ in range(26):
            adjacency += [[0]*26]

        os = [ord(d) - 97 for d in s]
        for c in intervals:
            oc = ord(c) - 97
            l, r = intervals[c]
            is_set = set()
            for d in os[l:r+1]:
                if len(is_set) == 26: break
                is_set.add(d)
                adjacency[oc][d] = 1

        adjacency = Matrix(adjacency)**32

        reachable = defaultdict(str)
        for c in intervals:
            for i in range(26):
                if adjacency[ord(c) - 97][i] == 1:
                    reachable[c] += chr(i+97)

        self.reachable = reachable
                        
        roots = set()
        
        for c in intervals:
            if self.is_root(c):
                roots.add(''.join(sorted(reachable[c])))
                
        ret = []
        for cs in roots:
            l, r = float("inf"), float("-inf")
            for c in cs:
                ll, rr = intervals[c]
                l = min(l, ll)
                r = max(r, rr)
            ret += [s[l:r+1]]

        return ret

import random
test_case = ''.join(random.choice(ALPHABET) for _ in range(10**5))

for i in range(100):
    print(i)
    Solution().maxNumOfSubstrings(test_case)