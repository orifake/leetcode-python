from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)


t = Solution()
print(t.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
