from collections import defaultdict
from math import gcd
from typing import *
import sys, resource

sys.setrecursionlimit(200000)

class Solution:

    def dfs0(self, u, parent, depth):
        self.depth_of[u] = depth
        for v in self.neighbours[u]:
            if v == parent: continue
            self.dfs0(v, u, depth+1)

    def dfs(self, u, parent, lookup):
        self.l_of[u] = lookup
        for v in self.neighbours[u]:
            if v == parent: continue

            l = lookup.copy()
            l[self.nums[u]] = u

            self.dfs(v, u, l)
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:

        self.neighbours = defaultdict(list)
        self.nums = nums
        self.l_of = dict()
        self.depth_of = dict()

        for [u, v] in edges:
            self.neighbours[u] += [v]
            self.neighbours[v] += [u]

        self.dfs0(0, 0, 0)
        self.dfs(0, 0, dict())

        ret = []
        for i in range(len(nums)):
            candidates = []
            b = nums[i]
            for o in self.l_of[i]:
                if gcd(o, b) != 1: continue

                v = self.l_of[i][o]
                candidates += [(self.depth_of[v], v)]

            if len(candidates) == 0:
                ret += [-1]
            else:
                ret += [max(candidates)[1]]

        return ret

s = Solution()
N = 2*10**4
k = s.getCoprimes([2]*N, [(i, i+1) for i in range(N-1)])
print(k[0:10])