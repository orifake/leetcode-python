from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                result += prices[i] - prices[i - 1]
        return result


t = Solution()
print(t.maxProfit([7, 6, 4, 3, 1]))
