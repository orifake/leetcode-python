from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices


t = Solution()
print(t.finalPrices([8, 4, 6, 2, 3]))
