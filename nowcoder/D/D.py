from functools import lru_cache

class Solution:
    lru_cache(None)
    def ans(self, bread, bev, N):
        if bread <= 0 and bev <= 0: return 0
        if N == len(self.packageSum): return float("inf")

        [this_bread, this_bev, cost] = self.packageSum[N]
        return min(self.ans(bread, bev, N+1), cost+self.ans(bread-this_bread, bev-this_bev, N+1))

    def minCost(self, breadNum, beverageNum, packageSum):
        self.breadNum = breadNum
        self.packageSum = packageSum

        return self.ans(breadNum, beverageNum, 0)

s = Solution()

print(s.minCost(5,60,[[3,36,120],[10,25,129],[5,50,250],[1,45,130],[4,20,119]]))