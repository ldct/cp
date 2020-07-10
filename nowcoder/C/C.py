class Solution:
    def solve(self, n, m):
        ret = 0
        frontier = set([n])

        while True:
            if m in frontier: return ret

            next = set()

            for x in frontier:
                if x+1 <= m:
                    next.add(x+1)
                next.add(x-1)
                if (x < m):
                    next.add(x**2)

            frontier = next
            ret += 1

s = Solution()

for m in range(1, 1000):
    for n in range(1, 1000):
        print(f"{n} {m}")
        print(s.solve(n, m))
        print("ok")

print(s.solve(2,1000))