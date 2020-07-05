#!/usr/bin/env pypy3

# Input: num = "9438957234785635408", k = 23
# Output: "0345989723478563548"

from collections import defaultdict

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = list(map(int, num))
        cost = defaultdict(list)

        for c in range(0, 10):
            smaller = 0
            for i in range(0, len(num)):
                if num[i] > c:
                    smaller += 1
                elif num[i] == c:
                    cost[c] += [(smaller, i)]

        prefix = []

        for d in range(0, 10):
            for c, i in cost[d]:
                if c > k:
                    continue
                else:
                    k -= c
                    num[i] = None
                    prefix += [d]

        if d == 10:
            assert(len(num) == 0)
            return ''.join(map(str, prefix))


        print(prefix, num, k)
        return num

s = Solution()
print(s.minInteger("9438957234785635408", 23))