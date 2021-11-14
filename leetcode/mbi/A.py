#!/usr/bin/env pypy3

from typing import *

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        bs = []
        mp = [-1]
        for beauty, price in items:
            bs += [beauty]
            mp += [max(mp[-1], price)]

        ret = []
        for q in queries:
            i = bisect.bisect(bs, q)
            if i > 0: i -= 1
            ret += [mp[i]]

        return ret

s = Solution()
print(s.maximumBeauty())