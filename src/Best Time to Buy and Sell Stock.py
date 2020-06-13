from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = sys.maxsize
        max = 0
        for i in prices:
            if i < min:
                min = i
            elif i - min > max:
                max = i - min
        return max